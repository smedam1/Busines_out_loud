from supabase import create_client, Client
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def get_magazine_url(name):
    base_url = os.environ.get("SUPABASE_URL")
    return f"{base_url}/storage/v1/object/public/magazine-pdfs/{name}"

def create_magazine_db(title, pdf_file, thumbnail_file, created_by):
    pdf_filename = None
    thumbnail_filename = None
    
    try:
        # 1. Upload PDF file
        pdf_filename = pdf_file.filename
        pdf_content = pdf_file.read()
        supabase.storage.from_("magazine-pdfs").upload(
            path=pdf_filename,
            file=pdf_content,
            file_options={"content-type": pdf_file.content_type, "upsert": "false"}
        )
        print(f"PDF file '{pdf_filename}' uploaded successfully.")
        pdf_url = supabase.storage.from_("magazine-pdfs").get_public_url(pdf_filename)
        print(f"PDF public URL: {pdf_url}")

        # 2. Upload thumbnail file (if provided)
        thumbnail_url = None
        if thumbnail_file:
            thumbnail_filename = thumbnail_file.filename
            thumbnail_content = thumbnail_file.read()
            supabase.storage.from_("magazine-thumbnails").upload(
                path=thumbnail_filename,
                file=thumbnail_content,
                file_options={"content-type": thumbnail_file.content_type, "upsert": "false"}
            )
            thumbnail_url = supabase.storage.from_("magazine-thumbnails").get_public_url(thumbnail_filename)
        print(f"Thumbnail file '{thumbnail_filename}' uploaded successfully." if thumbnail_file else "No thumbnail file provided.")

        # 3. Insert record into the database
        magazine_id = str(uuid.uuid4())
        response = supabase.table("magazine_details").insert({
            "id": magazine_id,
            "title": title,
            "pdf_url": pdf_url,
            "thumbnail_url": thumbnail_url,
            "created_by": created_by
        }).execute()
        print(f"response from database insert: {response}")
        
        if response.data:
            return {"status": "success", "data": response.data[0]}
        else:
            # This case might be hit if the insert fails for reasons other than an exception
            raise Exception("Failed to save magazine details to database.")

    except Exception as e:
        # Cleanup storage if any file was uploaded before the error
        if "Duplicate" in str(e) or "duplicate" in str(e):
             return {"status": "error", "message": "A file with this name already exists. Please rename your file."}

        if pdf_filename:
            supabase.storage.from_("magazine-pdfs").remove([pdf_filename])
        if thumbnail_filename:
            supabase.storage.from_("magazine-thumbnails").remove([thumbnail_filename])
        
        print(f"Error creating magazine: {e}")
        return {"status": "error", "message": str(e)}

def get_recent_magazines_db(limit=9):
    print(f"Fetching recent magazines with limit: {limit}")
    response = (
        supabase.table("magazine_details")
        .select("*")
        .order("created_at", desc=True)
        .range(0, limit - 1)
        .execute()
    )
    if response.data:
        return response.data
    return []

def get_magazine_details_db(magazine_id):
    print(f"Fetching magazine details for ID: {magazine_id}")
    response = (
        supabase.table("magazine_details").select("*").eq("id", magazine_id).execute()
    )
    if response.data:
        return response.data[0]
    return None

def delete_magazine_from_db(magazine_id):
    try:
        # 1. Get file URLs from the database record
        record_response = supabase.table("magazine_details").select("pdf_url, thumbnail_url").eq("id", magazine_id).single().execute()
        if not record_response.data:
            return {"status": "error", "message": "Magazine not found."}

        record = record_response.data
        pdf_url = record.get("pdf_url")
        thumbnail_url = record.get("thumbnail_url")
        
        # 2. Delete the database record first
        delete_db_response = supabase.table("magazine_details").delete().eq("id", magazine_id).execute()
        if not delete_db_response.data:
            raise Exception("Failed to delete magazine record from database.")

        # 3. Delete files from storage
        if pdf_url:
            pdf_filename = os.path.basename(pdf_url.split('?')[0])
            supabase.storage.from_("magazine-pdfs").remove([pdf_filename])

        if thumbnail_url:
            thumbnail_filename = os.path.basename(thumbnail_url.split('?')[0])
            supabase.storage.from_("magazine-thumbnails").remove([thumbnail_filename])

        return {"status": "success", "message": "Magazine deleted successfully."}
    except Exception as e:
        print(f"Error deleting magazine: {str(e)}")
        return {"status": "error", "message": str(e)}
