from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Intelligence Bug Diagnosis Platform is running"
    })


@app.route("/submit-bug", methods=["POST"])
def submit_bug():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No bug report data received"
        }), 400

    return jsonify({
        "message": "Bug report received successfully",
        "bug_report": data
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
