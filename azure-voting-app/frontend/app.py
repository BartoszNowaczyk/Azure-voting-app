from flask import Flask, send_from_directory, request, jsonify
import requests

app = Flask(__name__, static_folder="templates")

BACKEND_URL = "http://backend:5000"

@app.route('/')
def index():
    return send_from_directory("templates", "index.html")

@app.route('/votes')
def get_votes():
    response = requests.get(f"{BACKEND_URL}/votes")
    return response.json()

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    requests.post(f"{BACKEND_URL}/vote", json=data)
    return jsonify({"message": "Vote recorded"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
