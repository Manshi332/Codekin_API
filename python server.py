from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get("code", "")
    stdin = data.get("input", "")

    response = requests.post("https://api.jdoodle.com/v1/execute", json={
        "script": code,
        "language": "cpp17",
        "versionIndex": "0",
        "stdin": stdin,
        "clientId": "9aa5311d99810b3db7f4d6aaaa83d5a9",
        "clientSecret": "a09ed8c852ad4bf9e6e5ca1eadb08e693ab6d749e1d994e996cd9805a8d7791"
    })

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
