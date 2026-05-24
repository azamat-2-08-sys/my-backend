from flask import Blueprint, jsonify

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/profile")
def profile():
    return jsonify({
        "id": 1,
        "name": "Azamat",
        "role": "backend student"
    })
