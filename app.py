
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Welcome to ZeroOps MVP! Automate your DevOps here.")

@app.route("/health")
def health():
    return jsonify(status="healthy", uptime="99.99%")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
