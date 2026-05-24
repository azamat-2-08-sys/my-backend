from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import bcrypt

auth_routes = Blueprint("auth_routes", __name__)

users = []

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    users.append({
        "username": username,
        "password": hashed_password
    })

    return jsonify({"message": "User registered successfully"}), 201


@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = next((u for u in users if u["username"] == username), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        return jsonify({"error": "Wrong password"}), 401

    token = create_access_token(identity=username)

    return jsonify({"access_token": token})
