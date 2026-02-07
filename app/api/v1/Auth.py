from flask import request, jsonify
from flask_login import login_user, logout_user, login_required
from app.extensions import db
from app.core.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

def register(api):
    @api.route("/auth/register", methods=["POST"])
    def register_user():
        data = request.json
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 400

        user = User(
            email=email,
            username=username,
            password_hash=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"status": "ok", "user_id": user.id})

    @api.route("/auth/login", methods=["POST"])
    def login():
        data = request.json
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({"error": "Invalid credentials"}), 401

        login_user(user)
        return jsonify({"status": "ok", "user_id": user.id})

    @api.route("/auth/logout")
    @login_required
    def logout():
        logout_user()
        return jsonify({"status": "ok"})
