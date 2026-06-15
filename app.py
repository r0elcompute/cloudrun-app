import os
import socket
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Cloud Run",
        "Name": "Rodgers"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
