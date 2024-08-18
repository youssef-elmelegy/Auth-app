from flask import request, jsonify, make_response
from website.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
import random
from datetime import datetime, timedelta
from website.utils.generate_token_and_set_cookie import generate_token_and_set_cookie
from mailTrap.emails import send_verification_email, send_welcome_email, send_reset_password_email, send_reset_success_email
import os
from dotenv import load_dotenv
import secrets
from website.middleware.verifyToken import verify_token

load_dotenv()

def sign_up():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')

        if not email or not password or not name:
            raise ValueError("All fields are required")
        
        # print(f"Checking if user already exists for email: {email}")  # Debugging
        userAlreadyExists = User.query.filter_by(email=email).first()
        # print("User already exists")
        if userAlreadyExists:
            # print("User already exists")
            return jsonify({"success": False, "message": "User already exists"}), 400

        passwordhash = generate_password_hash(password, method='pbkdf2:sha256')
        verificationToken = str(random.randint(100000, 999999))
        
        expiration_time = datetime.utcnow() + timedelta(days=1)
        
        user = User(
            email=email,
            password=passwordhash,
            name=name,
            verificationToken=verificationToken,
            verificationTokenExpiresAt=expiration_time  # 24 hours
        )
        
        db.session.add(user)
        db.session.commit()
        # print(f"User {email} created successfully")  # Debugging
        
        # for u in User.query.all():
        #     print(f"User: {u.email}, Token: {u.verificationToken}, Expires At: {u.verificationTokenExpiresAt}")

        response = make_response(jsonify({
            "success": True,
            "message": "User created successfully",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "lastLogin": user.lastLogin,
                "isVerified": user.isVerified,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "verificationToken": user.verificationToken,
                "verificationTokenExpiresAt": user.verificationTokenExpiresAt
            }
        }), 201)
        generate_token_and_set_cookie(response, user.id)
        
        send_verification_email(user.email, verificationToken)
        
        
        return response
    except ValueError as e:
        # print(f"ValueError: {e}")  # Debugging
        return jsonify({"success": False, "message": str(e)}), 400
    except Exception as e:
        # print(f"Exception: {e}")  # Debugging
        return jsonify({"error": "An unexpected error occurred"}), 500

def verify_email():
    data = request.get_json()
    code = data.get('code')
    
    if not code:
        return jsonify({"success": False, "message": "Verification code is required"}), 400
    
    try:
        # print(f"Received verification code: {code}")
        
        code = code.strip()
        
        # for u in User.query.all():
        #     print(f"User: {u.email}, Token: {u.verificationToken}, Expires At: {u.verificationTokenExpiresAt}")
        
        
        # user = User.query.filter_by(
        #     verificationToken=code
        # ).filter(User.verificationTokenExpiresAt > datetime.utcnow()).first()
        
        user = User.query.filter_by(verificationToken=code).first()

        # print(user)
        if user and user.verificationTokenExpiresAt > datetime.utcnow():
            # Update user verification status
            user.isVerified = True
            user.verificationToken = None
            user.verificationTokenExpiresAt = None
            db.session.commit()

            # Send welcome email
            send_welcome_email(user.email, user.name)
            
            return jsonify({
                "success": True,
                "message": "Email verified successfully",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                    "isVerified": user.isVerified
                }
            }), 200
        else:
            # Handle case where user is not found or token is expired
            return jsonify({"success": False, "message": "Invalid or expired verification code"}), 400
        
        # if not user:
        #     return jsonify({"success": False, "message": "Invalid or expired verification code"}), 400
        
        
        # user.isVerified = True
        # user.verificationToken = None
        # user.verificationTokenExpiresAt = None
        # db.session.commit()
        
        # send_welcome_email(user.email, user.name)
        
        # return jsonify({
        #     "success": True,
        #     "message": "Email verified successfully",
        #     "user": {
        #         "id": user.id,
        #         "email": user.email,
        #         "name": user.name,
        #         "is_verified": user.isVerified
        #     }
        # }), 200
    except Exception as e:
        print("Error in verify_email:", e)
        return jsonify({"success": False, "message": "Server error"}), 500

def logout():
    response = make_response(
        jsonify({"success": True, "message": "Logged out successfully"})
    )
    
    # Clear the cookie by setting it with an expired date
    response.set_cookie(
        "token",
        value="",
        max_age=0,
        httponly=True,
        secure=os.getenv("NODE_ENV") == "production",
        samesite="Strict"
    )
    
    return response

def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(data)
    
    try:
        user = User.query.filter_by(email=email).first()
        print(user)
        if not user:
            return jsonify({"success": False, "message": "User not found"}), 404
        
        if not check_password_hash(user.password, password):
            print("pass")
            return jsonify({"success": False, "message": "Invalid credentials"}), 401
        
        user.lastLogin = datetime.utcnow()
        print("commit")
        db.session.commit()
        
        
        response = make_response(jsonify({
            "success": True,
            "message": "Logged in successfully",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "lastLogin": user.lastLogin,
                "isVerified": user.isVerified,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
        }))
        print("cookie")
        generate_token_and_set_cookie(response, user.id)

        return response
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
    
def forget_password():
    data = request.get_json()
    email = data.get('email')
    
    is_email = User.query.filter_by(email=email).first()
    
    if not is_email:
        return jsonify({"success": False, "message": "User not found"}), 404
    
    try:
        reset_token = secrets.token_hex(20)
        reset_token_expires_at = datetime.utcnow() + timedelta(days=1)  # 1 hour expiration
        
        is_email.resetPasswordToken = reset_token
        is_email.resetPasswordExpiresAt = reset_token_expires_at
        db.session.commit()
        
        
        client_url = os.getenv("CLIENT_URL")
        reset_link = f"{client_url}/reset-password/{reset_token}"
        send_reset_password_email(is_email.email, reset_link)
        
        return jsonify({"success": True, "message": "Password reset link sent to your email"}), 200
        
    except Exception as e:
        print("Error in forget_password:", e)
        return jsonify({"error": "An unexpected error occurred"}), 500
    
    # send_password_reset_email(email, "123456")
    
def reset_password(token):
    if request.method == 'GET':
        # You can return a simple message or redirect to a frontend page
        return "Please submit your new password via POST request."
    
    data = request.get_json()
    new_password = data.get('password')
    if not new_password:
        return jsonify({"success": False, "message": "Password is required"}), 400

    
    try:
        user = User.query.filter_by(resetPasswordToken=token).first()
        
        if not user:
            return jsonify({"success": False, "message": "Invalid or expired reset token"}), 400
        
        if user.resetPasswordExpiresAt < datetime.utcnow():
            return jsonify({"success": False, "message": "Invalid or expired reset token"}), 400
        
        hashedPassword = generate_password_hash(new_password, method='pbkdf2:sha256')
        
        user.password = hashedPassword
        user.resetPasswordToken = None
        user.resetPasswordExpiresAt = None
        db.session.commit()
        
        send_reset_success_email(user.email, user.name)
        
        return jsonify({"success": True, "message": "Password reset successfully"}), 200
    except Exception as e:
        print("Error in reset_password:", e)
        return jsonify({"error": "An unexpected error occurred"}), 500
        

def check_auth():
    
    try:
        user = User.query.get(request.user_id)
        if not user:
            return jsonify({"success": False, "message": "User not found"}), 404

        user_data = {
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "lastLogin": user.lastLogin,
                "isVerified": user.isVerified,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
            }
        }
        return jsonify({"success": True, "user": user_data}), 200
    except Exception as e:
        print(f"Error in check_auth: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

