from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/votes', methods=['GET'])
def get_votes():
    votes = {
        "Option A": redis_client.get("Option A") or 0,
        "Option B": redis_client.get("Option B") or 0,
    }
    return jsonify(votes)

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    choice = data.get('choice')
    if choice in ["Option A", "Option B"]:
        redis_client.incr(choice)
        return "Vote recorded", 200
    return "Invalid choice", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
