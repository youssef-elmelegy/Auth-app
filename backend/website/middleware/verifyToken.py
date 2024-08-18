from functools import wraps
from flask import request, jsonify
import jwt
import os

def verify_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({"success": False, "message": "Unauthorized - no token provided"}), 401
        try:
            secret_key = os.getenv("JWT_SECRET")
            decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
            if not decoded:
                return jsonify({"success": False, "message": "Unauthorized - invalid token"}), 401
            request.user_id = decoded['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({"success": False, "message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"success": False, "message": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorator
