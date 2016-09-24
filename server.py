from flask import Flask, render_template, redirect, request
from werkzeug import secure_filename
import os
import utils
import threading
from db import trainning_state, training_result
import time
import logging
import process

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/aljun/quant/quant_platform/uploads'

ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    res = []
    for task in trainning_state.objects:
        res.append(task)
    return render_template("index.html", tasks=res)


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        training = request.files['training']
        predict = request.files['predict']
        if training and allowed_file(training.filename) and predict and allowed_file(predict.filename):
            filename = secure_filename(training.filename)
            training.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            predict_name = secure_filename(predict.filename)
            predict.save(os.path.join(
                app.config['UPLOAD_FOLDER'], predict_name))
            useless_label = request.form['label'].strip().split(',')
            stock_id = request.form['id']
            target = request.form['target']
            if target not in useless_label:
                useless_label.append(target)
            if stock_id not in useless_label:
                useless_label.append(stock_id)
            train_data = utils.open_data(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
            predict_data = utils.open_data(os.path.join(
                app.config['UPLOAD_FOLDER'], predict_name))
            task_name = str(request.form['task'] +
                            time.strftime("%m%d%Y%H%M")).strip()
            train_data_col = train_data.columns.tolist()
            predict_data_col = predict_data.columns.tolist()
            for i in useless_label:
                if ' ' not in i and len(i)>0:
                    try:
                        train_data_col.remove(i)
                        predict_data_col.remove(i)
                    except ValueError:
                        pass
            if not utils.check_colums(train_data_col, predict_data_col):
                print "error"
            new_training = trainning_state(
                taskName=task_name,
                state="still training",
            )
            new_training.save()
            training = threading.Thread(target=process.main, args=(
                train_data, predict_data, target, train_data_col, task_name,stock_id))
            training.start()
            return redirect("/")
    return ""


@app.route("/task/<string:task_name>")
def task_detail(task_name):
    res = []
    for item in training_result.objects(taskName=task_name):
        res.append(item)
    return render_template("detail.html", details=res)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
