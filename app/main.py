from flask import Flask
import os

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 8080))

@app.route("/")
def home():
    return "Hello from DevOps HTTP App 🚀"

@app.route("/health")
def health():
    return {"status": "UP"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)