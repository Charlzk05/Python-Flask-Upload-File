from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["f"]
        uploadPath = os.path.join(os.path.abspath("./storage"), secure_filename(file.filename))
        file.save(uploadPath)
        return f"File Uploaded successfully to {uploadPath}"

if __name__ == "__main__":
    app.run(debug=True)