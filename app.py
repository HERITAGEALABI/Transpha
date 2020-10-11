from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download_file():
    try:
        return send_file('/file/transpha.exe')
    except Exception as e:
        return "Oops! Try again."
