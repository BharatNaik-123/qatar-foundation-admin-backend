from flask import Blueprint, request, jsonify
from models import db, Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from utils.validators import is_valid_email, is_valid_password, validate_required_fields
from utils.token import generate_reset_token

auth_bp = Blueprint('auth', __name__)


# SIGNUP
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    missing = validate_required_fields(data, ['full_name', 'email', 'password'])
    if missing:
        return jsonify({"status": "error", "message": f"Missing fields: {', '.join(missing)}"}), 400

    if not is_valid_email(data['email']):
        return jsonify({"status": "error", "message": "Invalid email format"}), 400

    if not is_valid_password(data['password']):
        return jsonify({"status": "error", "message": "Password must be 8+ chars with letters and numbers"}), 400

    if Admin.query.filter_by(email=data['email']).first():
        return jsonify({"status": "error", "message": "Email already registered"}), 400

    hashed_pw = generate_password_hash(data['password'])

    new_user = Admin(
        full_name=data['full_name'],
        email=data['email'],
        password_hash=hashed_pw
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"status": "success", "message": "User registered successfully"}), 201


# LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = Admin.query.filter_by(email=data.get('email')).first()

    if not user or not check_password_hash(user.password_hash, data.get('password')):
        return jsonify({"status": "error", "message": "Invalid email or password"}), 401

    login_user(user)

    return jsonify({"status": "success", "message": "Login successful"}), 200


# LOGOUT
@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"status": "success", "message": "Logged out"}), 200


# FORGOT PASSWORD
@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get('email')

    user = Admin.query.filter_by(email=email).first()

    if user:
        token = generate_reset_token(email)
        print(f"Reset link: http://localhost:5000/reset/{token}")

    return jsonify({"status": "success", "message": "If email exists, reset link sent"}), 200