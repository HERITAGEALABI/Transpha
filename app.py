from flask import Flask, send_from_directory, render_template, jsonify, make_response
import os, json

app = Flask(__name__)

def update():
    with open("db.json", "r+") as json_file:
        json_object = json.load(json_file)
        json_object["downloads"] += 1
        json_file.seek(0)  # rewind
        json.dump(json_object, json_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST", "GET"])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    # Returning file from appended path
    update()
    return send_from_directory(directory=uploads, filename=transpha.exe)
  

@app.route("/reset", methods=["POST", "GET"])
def reset(filename):
    with open("db.json", "r+") as json_file:
        json_object = json.load(json_file)
        json_object["downloads"] = 1
        json_file.seek(0)  # rewind
        json.dump(json_object, json_file)
        return True
    return False
  


# @app.route("/download", methods=["POST"])
# def download_file():
#     try:
#         res= make_response(send_file('file/transpha.exe', 
#                         mimetype='application/x-msdownload'))
#         res.headers['Content-Disposition'] = 'attachment; filename=transpha.exe'

#     except Exception as e:
#         res= jsonify({'error': "Oops! Try again."+str(e)})
#         res.status_code = 500
#     return res

if __name__ == "__main__":
    app.run(debug=True)
