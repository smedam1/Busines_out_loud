from flask import Flask, render_template, request, jsonify, redirect
from static.data.page_handler import *

from pyngrok import ngrok
import psutil
import os
import time
from dotenv import load_dotenv
import json
import re

from static.data.page_handler import *
from static.data.page_editor import *
from static.data.db_handler import *
from static.data.blogs import *
from static.data.global_functions import *

from static.data.page_handlers.builder import *
from static.data.page_handlers.general_elements.header import get_header, get_blogs_for_header
from static.data.page_handlers.general_elements.footer import get_footer
from flask_ngrok import run_with_ngrok

load_dotenv()

app = Flask(__name__)
CATEGORIES = [
    "business",
    "technology",
    "gcc",
    "semiconductor",
    "sustainability",
]

# blogs_by_category=get_blogs_for_header(limit=3)

@app.route("/<data>", methods=["GET"])
def central_route(data):
    print(f"Received request for central route with data: {data}")

    # Handling Category Pages From Central Route
    if data in CATEGORIES:
        res = get_category_page(category=data,page_data=None)
        if res == "error":
            return render_template("not_found/404.html"), 404
        else:
            return res





    # Handling Admin Pages From Central Route
    if data == "admin_login":
        return render_template("admin_pages/admin.html")
    if data == "admin_blogs":
        return render_template("admin_pages/blogs/admin_blogs.html")
    if data == "page_updater":
        return render_template("admin_pages/page_updater.html")
    





    
    if data == "get_blog_list":
        search_keyword = request.args.get("search_keyword")
        list_of_blogs, _ = get_blogs_list_db(
            search_keyword=search_keyword, page=1, per_page=1000
        )
        return jsonify({"status": "success", "blogs": list_of_blogs})
    
    if data == "get_main_pages":
        search_keyword = request.args.get("search_keyword")
        list_of_pages, _ = get_main_pages_db(
            search_keyword=search_keyword, page=1, per_page=1000
        )
        return jsonify({"status": "success", "pages": list_of_pages})
    
    if data == "get_paginated_business_cards":
        try:
            page = int(request.args.get("page", 1))
        except (ValueError, TypeError):
            page = 1
        if page < 1:
            page = 1
        data = get_paginated_business_cards_data(page=page)
        return jsonify(data)
    




    # Handling Upload Pages From Central Route
    if data == "manage_files":
        return render_template("admin_pages/manage_files.html")
    if data == "get_file_details":
        data = request.args
        print(f"Received data for get_file_details: {json.dumps(data, indent=2, ensure_ascii=False)}")
        bucket_name = data.get("bucket_name", None)
        if not bucket_name:
            return jsonify({"status": "error", "message": "Bucket name is required"}), 400
        file_details = get_file_details_db(bucket_name)
        if file_details["status"] == "error":
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": file_details.get(
                            "message", "Failed to retrieve file details"
                        ),
                    }
                ),
                500,
            )
        return jsonify({"status": "success", "data": file_details.get("data", [])}), 200






    # Handling Magazine Pages From Central Route
    if data == "magazine":
        return render_template("magazine_page/magazine_page.html")
    
    if data == "magazine_dev":
        return get_magazine_home_page()
        
    

    if data == "advertise_with_us":
        header_content = get_header()
        footer_content = get_footer()
        return render_template("missellanious/advertise_with_us.html", header=header_content, footer=footer_content)




    # When no matches found, return 404
    return render_template("not_found/404.html"), 404


# --------------------------------------------------------------------------------#
#                                 HOMEPAGE_ROUTE                                  #
# --------------------------------------------------------------------------------#


@app.route("/")
def index():
    return get_homepage(page_data=None)




# --------------------------------------------------------------------------------#
#                                 USER AUTH ROUTES                                #
# --------------------------------------------------------------------------------#

@app.route("/login")
def login():
    header_content = get_header()
    footer_content = get_footer()
    return render_template("user_pages/login.html", header=header_content, footer=footer_content)

@app.route("/register")
def register():
    header_content = get_header()
    footer_content = get_footer()
    return render_template("user_pages/register.html", header=header_content, footer=footer_content)

@app.route("/user_register", methods=["POST"])
def user_register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    if not all([username, email, password]):
        return jsonify({"status": "error", "message": "All fields are required"}), 400

    result = user_register_db(username, email, password)
    
    if result.get("status") == "success":
        user_data = result.get("data")
        return jsonify({"status": "success", "message": "Registration successful", "user": {"username": user_data.get("username"), "email": user_data.get("email")}}), 201
    else:
        return jsonify(result), 400

@app.route("/user_auth", methods=["POST"])
def user_auth():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({"status": "error", "message": "Email and password are required"}), 400

    result = user_login_db_check(email, password)

    if result.get("success"):
        # Here you would typically create a session for the user
        return jsonify({"status": "success", "message": "Login successful", "user": result}), 200
    else:
        return jsonify({"status": "error", "message": result.get("message", "Invalid credentials")}), 401


# --------------------------------------------------------------------------------#
#                              RENDERING ROUTES                                  #
# --------------------------------------------------------------------------------#



# @app.route("/news_waiting_page")
# def news_waiting_page():
#     return render_template(
#         "news_waiting_page.html",
#         blogs_by_category=get_blogs_for_header(limit=3),
#         desktop_nav_links=f"""{generate_header_dropdowns_html(blogs_by_category)}""",
#         mobile_nav_links=f"""{generate_mobile_accordion_html(blogs_by_category)}""",
#     )


# @app.route("/news_page")
# def news_page():
#     return render_template(
#         "news_page.html",
#         blogs_by_category=get_blogs_for_header(limit=3),
#         desktop_nav_links=f"""{generate_header_dropdowns_html(blogs_by_category)}""",
#         mobile_nav_links=f"""{generate_mobile_accordion_html(blogs_by_category)}""",
#     )




# @app.route("/advertise_with_us")
# def advertise_with_us():
#     return render_template(
#         "missellanious/advertise_with_us.html",
#         blogs_by_category=get_blogs_for_header(limit=3)
#         # ,
#         # desktop_nav_links=f"""{generate_header_dropdowns_html(blogs_by_category)}""",
#         # mobile_nav_links=f"""{generate_mobile_accordion_html(blogs_by_category)}""",
#     )


# @app.route("/career_page")
# def career_page():
#     return render_template(
#         "career_page.html",
#         blogs_by_category=get_blogs_for_header(limit=3),
#         desktop_nav_links=f"""{generate_header_dropdowns_html(blogs_by_category)}""",
#         mobile_nav_links=f"""{generate_mobile_accordion_html(blogs_by_category)}""",
#     )


# @app.route("/JD")
# def JD():
#     return render_template(
#         "JD.html",
#         blogs_by_category=get_blogs_for_header(limit=3),
#         desktop_nav_links=f"""{generate_header_dropdowns_html(blogs_by_category)}""",
#         mobile_nav_links=f"""{generate_mobile_accordion_html(blogs_by_category)}""",
#     )



# --------------------------------------------------------------------------------#
#                              ADMIN PAGE ROUTES                                 #
# --------------------------------------------------------------------------------#

@app.route("/admin_auth", methods=["POST"])
def admin_auth():
    data = request.json
    email = (
        sha256_hash(data.get("email"))
        if "@" in data.get("email", "a")
        else data.get("enc_email")
    )
    password = (
        sha256_hash(data.get("password"))
        if "@" in data.get("email", "a")
        else data.get("enc_pwd")
    )
    return admin_login_db_check(email, password)


# ------------------------------ ADMIN PAGE BLOG ------------------------------#


@app.route("/admin_blog_preview", methods=["POST"])
def admin_blog_preview():
    data = request.json
    blog_data = get_blog_preview( blog_data=data)
    if blog_data.get('status') == "not_found":
        return render_template("not_found/404.html"), 404
    if blog_data.get('status') == "error":
        return render_template("not_found/404.html"), 500
    if blog_data.get('status') == "redirect":
        redirect_url = blog_data.get("redirect_url")
        if redirect_url:
            # Redirect to the specified URL
            return redirect(redirect_url, code=301)
        else:
            # Show 403 page if no redirect URL is provided
            return render_template("not_found/404.html"), 403

    # Check if blog is deleted and handle redirect
    if blog_data.get("status") == "deleted":
        redirect_url = blog_data.get("redirect_url")
        if redirect_url:
            # Redirect to the specified URL
            from flask import redirect
            return redirect(redirect_url, code=301)
        else:
            return render_template("not_found/404.html"), 403

    return {
        "status": "success",
        "data": blog_data['html']
    }


@app.route("/admin_save_blog", methods=["POST"])
def admin_save_blog():
    data = request.json
    minimum_required_keys = [
        "mainImageUrl",
        "mainImageAlt",
        "blogTitle",
        "blogAuthor",
        "blogDate",
        "blogSummary",
        "dynamicSections",
        "blogCategory",
    ]
    for key in minimum_required_keys:
        if not data.get(key):
            return (
                jsonify({"status": "error", "message": f"{key} cannot be empty"}),
                400,
            )
    
    # Check if labels are provided or if they are marked as not mandatory
    labels_data = data.get("labels", {})
    labels_not_mandatory = data.get("labelsNotMandatory", False)
    
    # If labels are not marked as optional and no labels are provided, return error
    if not labels_not_mandatory and (not labels_data or not isinstance(labels_data, dict) or len(labels_data) == 0):
        return (
            jsonify({"status": "error", "message": "Labels are required. Please add at least one label or mark labels as not mandatory."}),
            400,
        )

    verification_status = admin_login_db_check(
        email=data.get("enc_email", ""), password=data.get("enc_pwd", "")
    )
    if not verification_status["success"]:
        return (
            jsonify({"status": "error", "message": "Admin authentication failed"}),
            403,
        )

    data["admin_name"] = verification_status["name"]

    if data.get("reason", "insert") == "insert":
        result = save_blogs_to_db(data)
    else:
        result = update_blogs_to_db(data)

    if result.get("status") == "error":
        return jsonify({"status": "error", "message": result.get("message")}), 400

    return (
        jsonify(
            {
                "status": "success",
                "message": "Blog saved successfully",
                "url": result.get("url", ""),
            }
        ),
        200,
    )


@app.route("/blog/<blog_id>")
def display_blog(blog_id):
    blog_data = get_blog_page(blog_id)
    if blog_data.get('status') == "not_found":
        return render_template("not_found/404.html"), 404
    if blog_data.get('status') == "error":
        return render_template("not_found/404.html"), 500
    if blog_data.get('status') == "redirect":
        redirect_url = blog_data.get("redirect_url")
        if redirect_url:
            # Redirect to the specified URL
            return redirect(redirect_url, code=301)
        else:
            # Show 403 page if no redirect URL is provided
            return render_template("not_found/404.html"), 403

    # Check if blog is deleted and handle redirect
    if blog_data.get("status") == "deleted":
        print(f"Blog {blog_id} is marked as deleted. Redirecting to {blog_data.get('redirect_url')}")
        redirect_url = blog_data.get("redirect_url")
        if redirect_url:
            # Redirect to the specified URL
            from flask import redirect
            return redirect(redirect_url, code=301)
        else:
            return render_template("not_found/404.html"), 403

    return blog_data['html']


@app.route("/delete_blog", methods=["POST"])
def delete_blog():
    data = request.json
    blog_id = data.get("blog_id")
    redirect_url = data.get("redirect_url")
    
    if not blog_id:
        return jsonify({"status": "error", "message": "Blog ID is required"}), 400
    
    # Mark blog as deleted with optional redirect URL
    result = delete_blog_from_db(blog_id, redirect_url)
    
    if result.get("status") == "success":
        return jsonify({
            "status": "success",
            "message": "Blog marked as deleted successfully",
            "redirect_url": redirect_url
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": result.get("message", "Failed to mark blog as deleted")
        }), 500
 
 
# --------------------------------------------------------------------------------#
#                           MAIN PAGES ROUTES                                    #
# --------------------------------------------------------------------------------#

@app.route("/update_main_page", methods=["POST"])
def update_main_page():
    data = request.json
    page_id = data.get("page_id")
    page_name = data.get("page_name")
    page_data = data.get("page_data")

    if not all([page_id, page_name, page_data]):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400

    verification_status = admin_login_db_check(
        email=data.get("enc_email", ""), password=data.get("enc_pwd", "")
    )
    if not verification_status["success"]:
        return (
            jsonify({"status": "error", "message": "Admin authentication failed"}),
            403,
        )

    result = update_main_page_db(page_id, page_data)
    if result["status"] == "success":
        return jsonify({"status": "success", "message": "Page updated successfully"}), 200
    else:
        return jsonify({"status": "error", "message": result.get("message", "Failed to update page")}), 500

@app.route("/delete_main_page", methods=["POST"])
def delete_main_page():
    data = request.json
    page_id = data.get("page_id")

    if not page_id:
        return jsonify({"status": "error", "message": "Page ID is required"}), 400

    verification_status = admin_login_db_check(
        email=data.get("enc_email", ""), password=data.get("enc_pwd", "")
    )
    if not verification_status["success"]:
        return (
            jsonify({"status": "error", "message": "Admin authentication failed"}),
            403,
        )

    result = delete_main_page_db(page_id)
    if result["status"] == "success":
        return jsonify({"status": "success", "message": "Page deleted successfully"}), 200
    else:
        return jsonify({"status": "error", "message": result.get("message", "Failed to delete page")}), 500

@app.route("/preview_main_page", methods=["POST"])
def preview_main_page():
    data = request.json
    # print(f"Received data for preview_main_page: {json.dumps(data, indent=2, ensure_ascii=False)}")
    page_data = data.get("page_data")
    page_id = data.get("page_id") # Not strictly needed for rendering, but good for context

    if not page_data:
        return jsonify({"status": "error", "message": "No page data provided for preview"}), 400
    
    if data.get("page_name") == "homepage":
        print("Rendering homepage preview")
        # If the page is the homepage, we can use the get_homepage function directly
        preview_html = get_homepage(page_data=page_data)
    else:
        # For other pages, we can use the get_main_page_html function
        preview_html = get_category_page(category=data.get("page_name"), page_data=page_data)


    
    return jsonify({"status": "success", "html": preview_html}), 200

# --------------------------------------------------------------------------------#
#                             UPLOAD FILES ROUTE                                 #
# --------------------------------------------------------------------------------#


@app.route("/upload_file", methods=["POST"])
def upload_file():
    try:
        if "file" not in request.files:
            return jsonify({"status": "error", "message": "No file part"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"status": "error", "message": "No selected file"}), 400

        # Get file extension
        file_extension = (
            file.filename.rsplit(".", 1)[1].lower() if "." in file.filename else ""
        )

        # Define allowed extensions
        image_extensions = {"png", "jpg", "jpeg", "gif", "webp", "bmp", "svg"}
        pdf_extensions = {"pdf"}

        # Check file type and determine bucket path
        if file_extension in image_extensions:
            bucket_path = "blog-images"
        elif file_extension in pdf_extensions:
            bucket_path = "magazine-pdfs"
        else:
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "File not supported. Only images (PNG, JPG, JPEG, GIF, WEBP, BMP, SVG) and PDF files are allowed.",
                    }
                ),
                400,
            )

        # Upload file to Supabase storage
        result = upload_file_to_storage(file, bucket_path)

        if result.get("status") == "success":
            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "File uploaded successfully",
                        "url": result.get("url", ""),
                        "filename": file.filename,
                    }
                ),
                200,
            )
        else:
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": result.get("message", "Failed to upload file"),
                    }
                ),
                500,
            )

    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return jsonify({"status": "error", "message": f"Upload failed: {str(e)}"}), 500




@app.route("/delete_file", methods=["POST"])
def delete_file():
    data = request.json
    print(
        f"Received data for delete_file: {json.dumps(data, indent=2, ensure_ascii=False)}"
    )

    if "file_name" not in data:
        return jsonify({"status": "error", "message": "File name is required"}), 400

    file_name = data["file_name"]
    result = delete_file_from_storage(file_name)

    if result["status"] == "success":
        return (
            jsonify(
                {
                    "status": "success",
                    "message": result.get("message", "File deleted successfully"),
                }
            ),
            200,
        )
    else:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": result.get("message", "Failed to delete file"),
                }
            ),
            500,
        )


# --------------------------------------------------------------------------------#
#                            MAGAZINE PAGE FUNCTIONS                             #
# --------------------------------------------------------------------------------#

@app.route("/create_magazine", methods=["POST"])
def create_magazine():
    try:
        if 'title' not in request.form or 'pdf_file' not in request.files:
            return jsonify({"status": "error", "message": "Title and PDF file are required fields."}), 400

        title = request.form['title']
        pdf_file = request.files['pdf_file']
        thumbnail_file = request.files.get('thumbnail_file') # Optional

        result = create_magazine_db(title=title, pdf_file=pdf_file, thumbnail_file=thumbnail_file)

        if result.get("status") == "success":
            return jsonify({
                "status": "success",
                "message": "Magazine created successfully.",
                "data": result.get("data")
            }), 201
        else:
            # Pass the specific error message from the handler
            return jsonify({
                "status": "error",
                "message": result.get("message", "An unknown error occurred during magazine creation.")
            }), 400 # Using 400 for client errors like duplicates
    except Exception as e:
        print(f"Server error in /create_magazine: {str(e)}")
        return jsonify({"status": "error", "message": f"An internal server error occurred: {str(e)}"}), 500

@app.route("/delete_magazine", methods=["POST"])
def delete_magazine():
    try:
        data = request.get_json()
        if not data or 'id' not in data:
            return jsonify({"status": "error", "message": "Magazine ID is required."}), 400

        magazine_id = data['id']
        result = delete_magazine_from_db(magazine_id)

        if result.get("status") == "success":
            return jsonify({
                "status": "success",
                "message": result.get("message", "Magazine deleted successfully.")
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": result.get("message", "Failed to delete magazine.")
            }), 500
    except Exception as e:
        print(f"Server error in /delete_magazine: {str(e)}")
        return jsonify({"status": "error", "message": f"An internal server error occurred: {str(e)}"}), 500


@app.route("/magazine/<magazine_url>")
def magazine_page_read_only(magazine_url):
    header_content = get_header()
    footer_content = get_footer()
    if not magazine_url:
        return render_template("not_found/404.html"), 404

    return render_template("magazine_page/magazine_page_read_only.html", header=header_content, footer=footer_content, pdf_url=magazine_url)

@app.route("/magazine_dev/<magazine_url>")
def magazine_dev_page_read_only(magazine_url):
    if not magazine_url:
        return render_template("not_found/404.html"), 404

    return get_magazine_page()

@app.route("/flipbook/<magazine_url>")
@app.route("/flipbook")
def magazine_page_flipbook_view(magazine_url=None):
    if magazine_url is None:
        magazine_url = request.args.get("magazine_url")

    if not magazine_url:
        return render_template("not_found/404.html"), 404
    
    header_content = get_header()
    footer_content = get_footer()
    print(f"Received request for magazine_id: {magazine_url}")
    page_number = request.args.get("page_number", "1")

    return render_template("magazine_page/magazine_page_flipbook.html", header=header_content, footer=footer_content, pdf_url=magazine_url, page_number=page_number)

# --------------------------------------------------------------------------------#
#                            AD MANAGER Functionalities                           #
# --------------------------------------------------------------------------------#

@app.route("/ad_manager", methods=["GET"])
def ad_manager():
    return render_template("admin_pages/ad_manager.html")

# Organizations API
@app.route("/api/organizations", methods=["GET"])
def get_organizations():
    organizations = get_organizations_db()
    return jsonify(organizations)

@app.route("/api/organizations", methods=["POST"])
def add_organization():
    data = request.form.to_dict()
    logo_file = request.files.get('org_logo')
    if logo_file:
        result = upload_file_to_storage(logo_file, 'organization-resources')
        if result['status'] == 'success':
            data['logo'] = result['url']
        else:
            return jsonify({"error": "Failed to upload logo", "message": result.get("message")}), 400
    
    # Add organization to database
    result = add_organization_db(data)
    
    if result.get("status") == "error":
        # Check for duplicate organization error
        if "already exists" in result.get("message", ""):
            return jsonify({"error": result["message"]}), 409  # 409 Conflict
        return jsonify({"error": result.get("message", "Failed to add organization")}), 400
        
    return jsonify(result.get("data")), 201

@app.route("/api/organizations/<int:org_id>", methods=["PUT"])
def update_organization(org_id):
    data = request.form.to_dict()
    logo_file = request.files.get('org_logo')
    if logo_file:
        result = upload_file_to_storage(logo_file, 'organization-resources')
        if result['status'] == 'success':
            data['logo'] = result['url']
        else:
            return jsonify({"error": "Failed to upload logo", "message": result.get("message")}), 400
    updated_org = update_organization_db(org_id, data)
    if updated_org:
        return jsonify(updated_org)
    return jsonify({"error": "Failed to update organization"}), 400

@app.route("/api/organizations/<int:org_id>", methods=["DELETE"])
def delete_organization(org_id):
    try:
        delete_organization_db(org_id)
        return jsonify({"message": "Organization deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to delete organization", "message": str(e)}), 500

# Ads API
@app.route("/api/ads", methods=["GET"])
def get_ads():
    ads = get_ads_db()
    return jsonify(ads)

@app.route("/api/ads_post", methods=["POST"])
def add_ad_post():
    try:
        data = request.form.to_dict()
        org_id = int(data['organization_id'])
        
        # Fetch organization name
        org_details_response = supabase.table("organization").select("organization").eq("id", org_id).single().execute()
        
        if org_details_response.data:
            data['organization'] = org_details_response.data['organization']
        else:
            # Handle case where organization is not found
            return jsonify({"error": f"Organization with ID {org_id} not found"}), 404
        
        # Remove organization_id as it's not a column in the 'ads' table
        del data['organization_id']

        image_file = request.files.get('ad_image')
        if image_file:
            result = upload_file_to_storage(image_file, 'ads-resources')
            if result['status'] == 'success':
                data['image'] = result['url']
            else:
                return jsonify({"error": "Failed to upload ad image", "message": result.get("message")}), 400
        new_ad = add_ad_db(data)
        if new_ad:
            return jsonify(new_ad), 201
        return jsonify({"error": "Failed to add ad"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/ads/<int:ad_id>", methods=["PUT"])
def update_ad(ad_id):
    try:
        data = request.form.to_dict()
        if 'organization_id' in data:
            org_id = int(data['organization_id'])
            # Fetch organization name
            org_details_response = supabase.table("organization").select("organization").eq("id", org_id).single().execute()
            if org_details_response.data:
                data['organization'] = org_details_response.data['organization']
            else:
                # Handle case where organization is not found
                return jsonify({"error": f"Organization with ID {org_id} not found"}), 404
            
            del data['organization_id']

        image_file = request.files.get('ad_image')
        if image_file:
            result = upload_file_to_storage(image_file, 'ads-resources')
            if result['status'] == 'success':
                data['image'] = result['url']
            else:
                return jsonify({"error": "Failed to upload ad image", "message": result.get("message")}), 400
        updated_ad = update_ad_db(ad_id, data)
        if updated_ad:
            return jsonify(updated_ad)
        return jsonify({"error": "Failed to update ad"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/ads/<int:ad_id>", methods=["DELETE"])
def delete_ad(ad_id):
    delete_ad_db(ad_id)
    return jsonify({"message": "Ad deleted"})

# --------------------------------------------------------------------------------#
#                                 TRIAL ROUTE                                    #
# --------------------------------------------------------------------------------#


@app.route("/trial")
def trial():
    return render_template("trial.html")

@app.route("/blog_trial/<blog_id>")
def blog_trial(blog_id):
    return get_blog_page(blog_id)

@app.route("/dynamic_render_trial")
def dynamic_render_trial():
    return get_homepage()


@app.route("/news_page_dev")
def news_page_dev():
    return render_template("blog_page/news_page_dev.html")


# --------------------------------------------------------------------------------#
#                               MAIN RUNNING SCRIPT                              #
# --------------------------------------------------------------------------------#


def kill_ngrok_processes():
    ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))
    # Kill using pyngrok
    try:
        ngrok.kill()
        print("Killed ngrok processes via pyngrok")
    except Exception as e:
        print(f"pyngrok kill error: {e}")

    # Find and kill by process name
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if "ngrok" in proc.info["name"].lower():
                print(f"Killing ngrok process with PID {proc.info['pid']}")
                psutil.Process(proc.info["pid"]).terminate()
                time.sleep(0.5)
                if psutil.pid_exists(proc.info["pid"]):
                    psutil.Process(proc.info["pid"]).kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Additional OS-specific commands
    try:
        if os.name == "nt":  # Windows
            os.system("taskkill /F /IM ngrok.exe")
        else:  # Linux/Mac
            os.system("pkill -f ngrok")
    except Exception as e:
        print(f"OS command error: {e}")

    # Wait to ensure processes are terminated
    time.sleep(2)


def main(t="ngrok"):
    if t == "ngrok":
        kill_ngrok_processes()
        run_with_ngrok(app)
        ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))
        ngrok_tunnel = ngrok.connect(
            addr="5000", proto="http", hostname="noble-raven-entirely.ngrok-free.app"
        )
        print("Public URL:", ngrok_tunnel.public_url)
        app.run()
    else:
        app.run(port=5000, debug=True, use_reloader=True)


if __name__ == "__main__":
    main(t="local")




# add a keyword input to the blogs when editing /adding a blog. --> DONE
# add another field as volume that is being returned with this. --> DONE

# you can add multiple keywords and volumes. (one keyword can have one volume) --> DONE

# also add a tickbos saying this blog does not need a keyword to be publish. --> DONE

# add multiple search for each author, title, keyword, category and subcategory. --> DONE

# re structure the admin panel. --> DONE
# track only h2 nd h3 tags in the blog for TOC. --> 

# add the login functionality in main page. and every other page. --> In Progress
# add the loading screen to the blogs. --> DONE

# add the ads manager and upload magazines to admin panel. --> DONE