from flask import Flask, render_template, redirect, request
from werkzeug import secure_filename
import os
import utils
import threading
from db import trainning_state
import time

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
        training = request.files['training]
        predict_data = request.files['test']
        if training and allowed_file(training.filename) and predict_data and allowed_file(predict_data.filename):
            filename = secure_filename(training.filename)
            training.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            predict_data_name = secure_filename(test.filename)
            predict_data.save(os.path.join(app.config['UPLOAD_FOLDER'], predict_data_name))
            uesless_label = request.form['label'].split(',')
            target = request.form['target']
            if target not in useless_label:
                useless_label.append(target)
            train_data = utils.open_data(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
            predict = utils.open_data(os.path.join(
                app.config['UPLOAD_FOLDER'], predict_data_name))
            task_name = request.form['task'] + strftime("%m/%d/%Y%H:%M")
            new_training = trainning_state(
                taskName=task_name,
                state="still training",
            )
            training = threading.Thread(target=process.main, args=(
                train_data, predict, target, uesless_label,task_name))
            training.start()
            return redirect("/")
    return ""


if __name__ == "__main__":
    app.run(debug=True)
