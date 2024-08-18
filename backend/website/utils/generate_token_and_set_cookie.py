import jwt
from flask import request, make_response
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

def generate_token_and_set_cookie(response, user_id):
    secret_key = os.getenv("JWT_SECRET")
    expires_in = timedelta(days=7)
    
    token = jwt.encode(
        {"user_id": user_id, "exp": datetime.utcnow() + expires_in},
        secret_key,
        algorithm="HS256"
    )

    response.set_cookie(
        "token",
        token,
        httponly=True,
        secure=os.getenv("NODE_ENV") == "production",
        samesite="Strict",
        max_age=expires_in
    )

    return token