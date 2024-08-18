from flask import Blueprint, Flask, render_template

from website.controllers.auth_controller import login, logout, sign_up, verify_email, forget_password, reset_password, check_auth
from website.middleware.verifyToken import verify_token


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/check-auth', methods=['GET'])
@verify_token
def check_auth_route():
    return check_auth()

auth_bp.route('/signup', methods=['POST'])(sign_up)
auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/logout', methods=['POST'])(logout)

auth_bp.route('/verify-email', methods=['POST'])(verify_email)
auth_bp.route('/forgot-password', methods=['POST'])(forget_password)

auth_bp.route('/reset-password/<token>', methods=['POST'])(reset_password)

# @auth_bp.route('/login')
# def login():
#     return '<h1>Login</h1>'


# @auth_bp.route('/logout')
# def logout():
#     return '<h1>Logout</h1>'

#http://localhost:5100/reset-password/b366bb22e6ac6868453b9e8c321d8d2ccdaa7fff
#http://127.0.0.1:5000/reset-password/ec22d26fd2828bcb04514a3f748c2dd07dd17d52