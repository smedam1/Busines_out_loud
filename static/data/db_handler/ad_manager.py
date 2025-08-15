from supabase import create_client, Client
from.files import delete_file_from_storage_by_url
from .general_function import get_chosen_orgs
from dotenv import load_dotenv
import os
import random
load_dotenv()

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)



def get_organizations_db():
    orgs_response = supabase.table("organization").select("*").order("created_at", desc=True).execute()
    if not orgs_response.data:
        return []

    organizations = orgs_response.data
    
    # Get ad counts for each organization
    for org in organizations:
        # Use the organization name to count ads
        count_response = supabase.table("ads").select("id", count="exact").eq("organization", org.get("organization")).execute()
        org["ad_count"] = count_response.count if count_response.count else 0
        
    return organizations

def add_organization_db(data):
    try:
        # Case-insensitive check for existing organization
        existing_org_response = supabase.table("organization").select("id").ilike("organization", data['organization']).execute()
        if existing_org_response.data:
            return {"status": "error", "message": "An organization with this name already exists."}
            
        response = supabase.table("organization").insert(data).execute()
        if response.data:
            return {"status": "success", "data": response.data[0]}
        return {"status": "error", "message": "Failed to add organization to database."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def update_organization_db(org_id, data):
    response = supabase.table("organization").update(data).eq("id", org_id).execute()
    return response.data[0] if response.data else None

def delete_organization_db(org_id):
    # First, get the organization record to find the name and logo URL
    org_response = supabase.table("organization").select("organization, logo").eq("id", org_id).single().execute()
    if not org_response.data:
        # If organization doesn't exist, we can't proceed.
        raise Exception("Organization not found")

    organization_name = org_response.data.get("organization")
    logo_url = org_response.data.get("logo")

    # Handle associated ads using the organization name
    if organization_name:
        ads_response = supabase.table("ads").select("id, image").eq("organization", organization_name).execute()
        if ads_response.data:
            # Delete ad images from storage
            for ad in ads_response.data:
                if ad.get("image"):
                    delete_file_from_storage_by_url(ad.get("image"))
            # Delete ads from the database
            ad_ids = [ad['id'] for ad in ads_response.data]
            supabase.table("ads").delete().in_("id", ad_ids).execute()

    # Then, handle the organization's logo
    if logo_url:
        delete_file_from_storage_by_url(logo_url)

    # Finally, delete the organization record
    response = supabase.table("organization").delete().eq("id", org_id).execute()
    return response.data

def get_ads_db():
    response = supabase.table("ads").select("*").order("created_at", desc=True).execute()
    return response.data if response.data else []

def add_ad_db(data):
    response = supabase.table("ads").insert(data).execute()
    return response.data[0] if response.data else None

def update_ad_db(ad_id, data):
    response = supabase.table("ads").update(data).eq("id", ad_id).execute()
    return response.data[0] if response.data else None

def delete_ad_db(ad_id):
    # First, get the ad record to find the image URL
    ad_response = supabase.table("ads").select("image").eq("id", ad_id).single().execute()
    if ad_response.data and ad_response.data.get("image"):
        delete_file_from_storage_by_url(ad_response.data.get("image"))
        
    # Then, delete the ad record from the database
    response = supabase.table("ads").delete().eq("id", ad_id).execute()
    return response.data

# def get_ads_db(data:dict):
#     """
#     Fetch ads from the database based on the provided filters.
    
#     Args:
#         data (dict): {"aspect_ratio": "16:9", "number_of_ads": "5"}
    
#     Returns:
#         list: List of ads matching the criteria.

#     Logic: 
#         we first get a list of orgs based on their weightage, we choose one org for each ad and then randomly choose one ad ffrom each org based on the aspect ratio.
#     """
#     aspect_ratio = data.get("aspect_ratio")
#     number_of_ads = int(data.get("number_of_ads", 1))

#     chosen_orgs = get_chosen_orgs(k=number_of_ads)
#     ads = []
#     for org in chosen_orgs:
#         org_ads_response = supabase.table("ads").select("*").eq("organization", org).eq("aspect_ratio", aspect_ratio).execute()
#         if org_ads_response.data:
#             ads.append(random.choice(org_ads_response.data))
    
#     return ads if ads else []  # Return an empty list if no ads found


def get_ads_db():
    response = supabase.table("ads").select("*").order("created_at", desc=True).execute()
    return response.data if response.data else []

def get_orgs_db(org_id):
    response = supabase.table("organization").select("organization").eq("id", org_id).single().execute()
    return response