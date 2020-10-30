from flask import Flask, send_from_directory, render_template, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST", "GET"])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    # Returning file from appended path
    return send_from_directory(directory=uploads, filename=transpha.exe)
  
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