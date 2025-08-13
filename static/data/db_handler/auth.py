from supabase import create_client, Client

from dotenv import load_dotenv
import os

load_dotenv()

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

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

def user_register_db(username, email, password):
    from .general_function import sha256_hash
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
    from .general_function import sha256_hash
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
