import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join("data", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return jsonify({
        "message": "Intelligence Bug Diagnosis Platform is running"
    })


@app.route("/submit-bug", methods=["POST"])
def submit_bug():
    data = request.form
    uploaded_file = request.files.get("bugFile")

    if not data:
        return jsonify({
            "error": "No bug report data received"
        }), 400

    file_name = None

    if uploaded_file and uploaded_file.filename:
        file_name = secure_filename(uploaded_file.filename)

        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        uploaded_file.save(file_path)

        print("Uploaded file:", file_name)
        print("Saved to:", file_path)

    return jsonify({
        "message": "Bug report received successfully",
        "bug_report": data.to_dict(),
        "file_name": file_name
    }), 200


if __name__ == "__main__":
    app.run(debug=True)