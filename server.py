from flask import Flask, render_template, redirect, request
from werkzeug import secure_filename
import os
import process
import threading
from state_db import State
app = Flask(__name__)

UPLOAD_FOLDER = '/Users/aljun/quant/quant_platform/uploads'

ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uesless_label = request.form['label'].split(',')
            target = request.form['target']
            data = process.open_data(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
#            new_training = State(
#                name=filename,
#                path=os.path.join(app.config['UPLOAD_FOLDER'], filename),
#                state="still training",
#                clfPath=""
#            )
            training = threading.Thread(target=process.train, args=(
                data, uesless_label, target, filename))
            training.start()
            return redirect("/")
    return ""


if __name__ == "__main__":
    app.run(debug=True)
