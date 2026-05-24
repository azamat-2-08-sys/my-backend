from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    return jsonify({
        "message": "Protected profile",
        "user": current_user
    })
