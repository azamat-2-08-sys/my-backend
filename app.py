from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running",
        "status": "ok"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/profile")
def profile():
    return jsonify({
        "id": 1,
        "name": "Azamat",
        "role": "backend student"
    })

app.run(host="0.0.0.0", port=5000)
