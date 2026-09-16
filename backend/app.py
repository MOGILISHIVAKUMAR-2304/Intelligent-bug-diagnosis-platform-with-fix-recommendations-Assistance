from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Intelligence Bug Diagnosis Platform is running"
    })


@app.route("/submit-bug", methods=["POST"])
def submit_bug():
    data = request.get_json()

    return jsonify({
        "message": "Bug report received",
        "bug_report": data
    })


if __name__ == "__main__":
    app.run(debug=True)
