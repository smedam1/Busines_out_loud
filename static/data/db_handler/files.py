from supabase import create_client, Client
from .general_function import format_file_size
from dotenv import load_dotenv
import os

load_dotenv()

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

import uuid

def upload_file_to_storage(file, bucket_name):
    try:
        # Read file content
        file_content = file.read()
        
        # Sanitize filename to be URL-friendly
        file_name = f"{uuid.uuid4()}-{file.filename.replace(' ', '_')}"

        # Upload to Supabase storage
        response = supabase.storage.from_(bucket_name).upload(
            path=file_name,
            file=file_content,
            file_options={"content-type": file.content_type, "upsert": "false"},
        )

        # Retrieve the public URL
        public_url = supabase.storage.from_(bucket_name).get_public_url(file_name)
        
        return {"status": "success", "url": public_url}

    except Exception as e:
        error_message = str(e)
        print(f"Error uploading to storage: {error_message}")
        if "Duplicate" in error_message or "duplicate" in error_message:
            return {"status": "error", "message": "A file with this name already exists. Please rename your file."}
        return {"status": "error", "message": error_message}


def get_file_details_db(bucket_name, user_id):
    user_id = user_id if user_id is not None else "internal"
    if bucket_name == 'magazine-pdfs':
        try:
            response = supabase.table("magazine_details").select("id, title, pdf_url, thumbnail_url").eq("created_by", user_id).order("created_at", desc=True).execute()
            if response.data:
                transformed_data = []
                for row in response.data:
                    transformed_data.append({
                        "id": row.get("id"),
                        "name": row.get("title"),
                        "public_url": row.get("pdf_url"),
                        "thumbnail_url": row.get("thumbnail_url"),
                        "size": None
                    })
                return {"status": "success", "data": transformed_data}
            else:
                return {"status": "success", "data": []}
        except Exception as e:
            print(f"Error getting magazine details from DB: {str(e)}")
            return {"status": "error", "message": str(e), "data": []}
            
    try:
        # List all files in the specified bucket
        response = supabase.storage.from_(bucket_name).list()

        if not response:
            return {
                "status": "error",
                "message": "Failed to retrieve files",
                "data": [],
            }

        file_details = []
        if response and len(response) > 0 and response[0].get("name") is not None:
            public_url = supabase.storage.from_(bucket_name).get_public_url(
                response[0]["name"]
            )
            for file in response:
                # Get public URL for each file
                temp = (
                    public_url.split("storage")[0]
                    + "storage/v1/object/public/"
                    + bucket_name
                    + "/"
                    + file["name"]
                )

                file_info = {
                    "name": file["name"],
                    "size": format_file_size(file["metadata"]["size"]),
                    "id": file["id"],
                    "public_url": temp,
                    "thumbnail_url": None
                }
                file_details.append(file_info)
            return {"status": "success", "data": file_details, "public_url": public_url}
        return {"status": "success", "data": [], "public_url": ""}

    except Exception as e:
        # Cleanup storage if any file was uploaded before the error
        print(f"Error getting file details: {str(e)}")
        return {"status": "error", "message": str(e), "data": []}


def delete_file_from_storage_by_url(url):
    if not url or 'storage/v1/object/public' not in url:
        print(f"Invalid or empty URL provided for deletion: {url}")
        return
    try:
        # Extract bucket name and file name from the URL
        # e.g., https://<project>.supabase.co/storage/v1/object/public/bucket-name/file-name.png
        url_path = url.split('storage/v1/object/public/')[1]
        parts = url_path.split('/')
        bucket_name = parts[0]
        file_name = '/'.join(parts[1:]).split('?')[0] # Handle filenames with paths and remove query params
        
        print(f"Attempting to delete '{file_name}' from bucket '{bucket_name}'...")
        response = supabase.storage.from_(bucket_name).remove([file_name])
        print(f"Successfully deleted {file_name} from bucket {bucket_name}.")

    except Exception as e:
        print(f"Error deleting file from storage by URL '{url}': {e}")

def delete_file_from_storage(file_name):
    try:
        # This function is kept for general purpose deletion (e.g., blog images)
        # but is no longer used for deleting magazines. See delete_magazine_from_db.
        file_extension = file_name.lower().split(".")[-1]

        if file_extension in ["jpg", "jpeg", "png", "gif", "bmp", "webp", "svg"]:
            bucket_name = "blog-images"
        elif file_extension == "pdf":
            bucket_name = "magazine-pdfs"
        elif file_name == ".emptyFolderPlaceholder":
            bucket_name = "blog-images"
        else:
            return {
                "status": "error",
                "message": "Unsupported file type. Only images and PDFs are allowed.",
            }

        response = supabase.storage.from_(bucket_name).remove([file_name])

        if not response:
            return {"status": "error", "message": "Failed to delete file"}

        return {
            "status": "success",
            "message": f"File '{file_name}' deleted successfully from {bucket_name}",
        }

    except Exception as e:
        print(f"Error deleting file from storage: {str(e)}")
        return {"status": "error", "message": str(e)}
