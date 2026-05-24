from flask import Flask, jsonify
from routes.user_routes import user_routes

app = Flask(__name__)

app.register_blueprint(user_routes)

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
