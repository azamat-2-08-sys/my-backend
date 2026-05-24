from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from routes.user_routes import user_routes
from routes.auth_routes import auth_routes

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "my-super-long-secret-key-for-jwt-auth-123456789"

JWTManager(app)
CORS(app)

app.register_blueprint(user_routes)
app.register_blueprint(auth_routes)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

app.run(host="0.0.0.0", port=5000)
