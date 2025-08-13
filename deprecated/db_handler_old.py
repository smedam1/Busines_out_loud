from supabase import create_client, Client

from dotenv import load_dotenv
import os

load_dotenv()

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

from .html_templates import *
import time
import uuid

# --------------------------------------------------------------------------------#
#                           HOMEPAGE HELPER FUNCTIONS                            #
# --------------------------------------------------------------------------------#


def get_blogs_list_db(search_keyword, page=1, per_page=100, include_deleted=False):
    print(
        f"Searching blogs with keyword: {search_keyword}, page: {page}, per_page: {per_page}"
    )

    offset = (page - 1) * per_page

    # Use count='exact' to get the total number of rows matching the query
    query = supabase.table("blogs").select("*", count="exact")
    
    # Exclude deleted blogs unless specifically requested
    if not include_deleted:
        query = query.neq("status", "deleted")

    if not search_keyword or search_keyword.strip() == "":
        response = (
            query.order("created_at", desc=True)
            .range(offset, offset + per_page - 1)
            .execute()
        )
    else:
        search_term = f'%{search_keyword.replace(" ", "_").lower()}%'
        response = (
            query.or_(f"id.ilike.{search_term},category.ilike.{search_term}")
            .order("created_at", desc=True)
            .range(offset, offset + per_page - 1)
            .execute()
        )

    # The response object now contains 'data' and 'count'
    if response.data:
        return response.data, response.count
    return [], 0


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


# --------------------------------------------------------------------------------#
#                               BLOGS FUNCTIONS                                  #
# --------------------------------------------------------------------------------#

def get_blogs_by_category(category):
    response = (
        supabase.table("blogs")
        .select("*")
        .eq("category", category)
        .neq("status", "deleted")
        .order("created_at", desc=True)
        .execute()
    )
    return response.data if response.data else []

def get_blog(blog_id, render=False):
    response = supabase.table("blogs").select("*").eq("id", blog_id).execute()
    data = response.data[0] if len(response.data) > 0 else None
    if render:
        NEWSPAGE_BLANK_TEMPLATE = NEWSPAGE_BLANK_TEMPLATE.replace(
            "[[meta tags]]", data["meta_tags"]
        )
        return NEWSPAGE_BLANK_TEMPLATE
    return data


def handle_blog(
    blog_id: str = None,
    insert_data: dict = None,
    update_data: dict = None,
    operation: str = None,
):
    if operation == "insert":
        if insert_data is None:
            raise ValueError("insert_data must be provided for insert operation")
        # Insert a new blog
        response = supabase.table("blogs").insert(insert_data).execute()
        return response.data

    if operation == "update":
        if blog_id is None or update_data is None:
            raise ValueError(
                "blog_id and update_data must be provided for update operation"
            )
        # Update an existing blog
        response = (
            supabase.table("blogs").update(update_data).eq("id", blog_id).execute()
        )
        return response.data

    if operation == "delete":
        if blog_id is None:
            raise ValueError("blog_id must be provided for delete operation")
        # Delete a blog
        response = supabase.table("blogs").delete().eq("id", blog_id).execute()
        return response.data


def get_leadership_details():
    response = supabase.table("leadership_table").select("*").execute()
    return response.data[0] if response.data else None


def save_blogs_to_db(blog_data):
    modified_data = {}
    blog_id = blog_data.get("blogTitle", "").replace(" ", "_").lower()
    modified_data["id"] = blog_id
    modified_data["created_by"] = blog_data.get("admin_name", "")
    modified_data["status"] = blog_data.get("status", "draft")

    # Extract category and SEO information for separate storage if needed
    modified_data["category"] = blog_data.get("blogCategory", "")
    # Sub-category commented out as requested
    # modified_data['sub_category'] = blog_data.get('blogSubCategory', '')
    
    # Extract and store labels in JSON format
    labels_data = blog_data.get("labels", {})
    modified_data["labels"] = labels_data if isinstance(labels_data, dict) else {}

    # Generate meta tags from SEO data
    seo_title = blog_data.get("seoTitle", "") or blog_data.get("blogTitle", "")
    seo_description = blog_data.get("seoMetaDescription", "") or blog_data.get(
        "blogSummary", ""
    )
    seo_canonical = (
        blog_data.get("seoCanonicalUrl", "")
        or f"{blog_data.get('base_url', '')}/blog/{modified_data['id']}"
    )

    # Create meta tags HTML
    meta_tags = f"""<title>{seo_title}</title>
    <meta name="description" content="{seo_description}">
    <meta property="og:title" content="{seo_title}">
    <meta property="og:description" content="{seo_description}">
    <meta property="og:image" content="{blog_data.get('mainImageUrl', '')}">
    <meta property="og:url" content="{seo_canonical}">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{seo_title}">
    <meta name="twitter:description" content="{seo_description}">
    <meta name="twitter:image" content="{blog_data.get('mainImageUrl', '')}">
    <link rel="canonical" href="{seo_canonical}">"""

    modified_data["meta_tags"] = meta_tags

    # Store the base_url before cleaning up for the return URL
    base_url = blog_data.get("base_url", "")

    # Clean up fields before storing in json_data
    fields_to_remove = ["admin_name", "status", "enc_email", "enc_pwd", "base_url", "labels"]
    for field in fields_to_remove:
        if field in blog_data:
            del blog_data[field]

    # Store the complete blog data including category and SEO information
    modified_data["json_data"] = blog_data
    
    # Check if a blog with the same ID exists and is in deleted state
    try:
        existing_blog_response = supabase.table("blogs").select("*").eq("id", blog_id).execute()
        existing_blog = existing_blog_response.data[0] if existing_blog_response.data else None
        
        if existing_blog and existing_blog.get("status") == "deleted":
            # Update the existing deleted blog instead of inserting
            print(f"Found existing deleted blog with ID: {blog_id}. Updating instead of inserting.")
            
            # Clear redirect URL when updating from deleted state
            modified_data["redirect_url"] = None
            
            # Get existing blog history and append to it
            if existing_blog and "history" in existing_blog:
                modified_data["history"] = existing_blog["history"]
                modified_data["history"].append(
                    {
                        "admin_name": modified_data["created_by"],
                        "date": blog_data.get("blogDate", ""),
                        "action": "restored_from_deleted",
                    }
                )
            else:
                modified_data["history"] = [
                    {
                        "admin_name": modified_data["created_by"],
                        "date": blog_data.get("blogDate", ""),
                        "action": "restored_from_deleted",
                    }
                ]
            
            # Update the existing blog
            response = supabase.table("blogs").update(modified_data).eq("id", blog_id).execute()
            
            if response.data:
                response.data[0]["url"] = f"{base_url}/blog/{modified_data['id']}"
                return response.data[0]
            else:
                return {
                    "status": "error",
                    "message": "Failed to update existing deleted blog.",
                }
        else:
            # Insert new blog (original logic)
            modified_data["history"] = [
                {
                    "admin_name": modified_data["created_by"],
                    "date": blog_data.get("blogDate", ""),
                }
            ]
            
            # Debug: Print what data is being stored
            print(f"Inserting new blog with data: {modified_data}")
            
            response = supabase.table("blogs").insert(modified_data).execute()
            
            # Use the stored base_url for the return URL
            response.data[0]["url"] = f"{base_url}/blog/{modified_data['id']}"
            return response.data[0]
            
    except Exception as e:
        print(f"Error saving blog to database: {e}")
        error_str = str(e)
        print(f"Error string: {error_str}")
        if (
            "23505" in error_str
            and "duplicate key value violates unique constraint" in error_str
        ):
            return {
                "status": "error",
                "message": "Blog with this title already exists.",
            }
        return {
            "status": "error",
            "message": f"Failed to save blog: {str(e)}",
        }


def update_blogs_to_db(blog_data):
    blog_id = blog_data.get("blog_id")
    if not blog_id:
        return {"status": "error", "message": "Blog ID is required for update."}

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



def delete_blog_from_db(blog_id, redirect_url=None):
    print(f"Marking blog as deleted with ID: {blog_id}")
    
    # Prepare update data
    update_data = {
        "status": "deleted",
        "meta_tags": ""  # Clear meta tags when marking as deleted
    }
    
    # Add redirect URL if provided
    if redirect_url:
        update_data["redirect_url"] = redirect_url
    
    # Update the blog status instead of deleting
    response = supabase.table("blogs").update(update_data).eq("id", blog_id).execute()
    
    if response.data:
        return {"status": "success", "message": "Blog marked as deleted successfully."}
    return {"status": "error", "message": "Blog not found or could not be updated."}


# --------------------------------------------------------------------------------#
#                             UPLOAD PAGE FUNCTIONS                               #
# --------------------------------------------------------------------------------#


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


def get_file_details_db(bucket_name):
    if bucket_name == 'magazine-pdfs':
        try:
            response = supabase.table("magazine_details").select("id, title, pdf_url, thumbnail_url").order("created_at", desc=True).execute()
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


# --------------------------------------------------------------------------------#
#                             ADMIN PAGE FUNCTIONS                               #
# --------------------------------------------------------------------------------#


def admin_login_db_check(email, password):
    print(f"Attempting admin login with email: {email} and \n password: {password}")
    response = (
        supabase.table("admin users")
        .select("*")
        .eq("email", email)
        .eq("password", password)
        .execute()
    )
    if response.data:
        return {
            "success": True,
            "email": email,
            "name": response.data[0]["username"],
            "enc_email": response.data[0]["email"],
            "enc_pwd": response.data[0]["password"],
        }
    return {"success": False, "email": email}

# --------------------------------------------------------------------------------#
#                               USER AUTH FUNCTIONS                              #
# --------------------------------------------------------------------------------#

def user_register_db(username, email, password):
    from .global_functions import sha256_hash
    try:
        # Check if user already exists
        response = supabase.table("users").select("id").eq("email", email).execute()
        if response.data:
            return {"status": "error", "message": "User with this email already exists."}

        # Insert new user
        response = supabase.table("users").insert({
            "username": username,
            "email": email,
            "password": sha256_hash(password)
        }).execute()

        if response.data:
            return {"status": "success", "message": "User registered successfully.", "data": response.data[0]}
        else:
            return {"status": "error", "message": "Failed to register user."}
    except Exception as e:
        print(f"Error registering user: {e}")
        return {"status": "error", "message": str(e)}

def user_login_db_check(email, password):
    from .global_functions import sha256_hash
    try:
        hashed_password = sha256_hash(password)
        response = supabase.table("users").select("*").eq("email", email).eq("password", hashed_password).execute()
        
        if response.data:
            user = response.data[0]
            return {
                "success": True,
                "username": user["username"],
                "email": user["email"],
            }
        return {"success": False, "message": "Invalid email or password."}
    except Exception as e:
        print(f"Error during user login check: {e}")
        return {"success": False, "message": str(e)}


# --------------------------------------------------------------------------------#
#                            MAGAZINE PAGE FUNCTIONS                             #
# --------------------------------------------------------------------------------#

def get_magazine_url(name):
    base_url = os.environ.get("SUPABASE_URL")
    return f"{base_url}/storage/v1/object/public/magazine-pdfs/{name}"

def create_magazine_db(title, pdf_file, thumbnail_file):
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
            "thumbnail_url": thumbnail_url
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


# --------------------------------------------------------------------------------#
#                            AD MANAGER FUNCTIONS                                #
# --------------------------------------------------------------------------------#

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