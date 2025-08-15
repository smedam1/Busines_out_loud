from supabase import create_client, Client
import hashlib
from dotenv import load_dotenv
import os
import random
load_dotenv()

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def sha256_hash(input_string):
    encoded_string = input_string.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded_string)
    return sha256_hash.hexdigest()


def get_page_data(page_name: str):
    response = (
        supabase.table("main_pages").select("*").eq("page_name", page_name).execute()
    )
    return response.data[0] if response.data else None

def format_file_size(size_bytes):
    """Convert bytes to human readable format (B, KB, MB, GB, TB)"""
    if size_bytes is None:
        return "N/A"
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    try:
        size_bytes = float(size_bytes)
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        return f"{size_bytes:.1f} {size_names[i]}"
    except (ValueError, TypeError):
        return "N/A"
    
def get_leadership_details():
    response = supabase.table("leadership_table").select("*").execute()
    return response.data[0] if response.data else None

def get_main_pages_db(search_keyword, page=1, per_page=100, include_deleted=False):
    print(
        f"Searching main pages with keyword: {search_keyword}, page: {page}, per_page: {per_page}"
    )

    offset = (page - 1) * per_page

    query = supabase.table("main_pages").select("*", count="exact")
    
    # Exclude pages with status 'DELETED'
    query = query.or_(f'page_data->>status.is.null,page_data->>status.neq.DELETED')

    if not search_keyword or search_keyword.strip() == "":
        response = (
            query.order("updated_at", desc=True)
            .range(offset, offset + per_page - 1)
            .execute()
        )
    else:
        search_term = f'%{search_keyword.lower()}%'
        response = (
            query.ilike("page_name", search_term)
            .order("updated_at", desc=True)
            .range(offset, offset + per_page - 1)
            .execute()
        )

    if response.data:
        return response.data, response.count
    return [], 0

def update_main_page_db(page_id, page_data):
    try:
        response = supabase.table("main_pages").update({
            "page_data": page_data,
            "updated_at": "now()" # Supabase function to set current timestamp
        }).eq("page_id", page_id).execute()
        
        if response.data:
            return {"status": "success", "data": response.data[0]}
        else:
            return {"status": "error", "message": "Page not found or could not be updated."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def delete_main_page_db(page_id):
    try:
        # First, get the current page_data
        page_response = supabase.table("main_pages").select("page_data").eq("page_id", page_id).single().execute()
        
        if not page_response.data:
            return {"status": "error", "message": "Page not found."}

        page_data = page_response.data.get("page_data", {})
        
        # Update the status to 'DELETED'
        page_data['status'] = 'DELETED'
        
        # Update the record in the database
        response = supabase.table("main_pages").update({
            "page_data": page_data,
            "updated_at": "now()"
        }).eq("page_id", page_id).execute()

        if response.data:
            return {"status": "success", "message": "Page status set to DELETED."}
        else:
            return {"status": "error", "message": "Page not found or could not be updated."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def get_chosen_orgs(k=1):
    """
    Choose one or more organizations based on their weights.
    
    :param data: List of dictionaries with 'name' and 'percentage'.
    :param k: Number of selections to make.
    :return: List of chosen organization names.
    """
    data = supabase.table("organization").select("organization,percentage").execute().data
    names = [item["organization"] for item in data]
    weights = [item["percentage"] for item in data]
    
    return random.choices(names, weights=weights, k=k)