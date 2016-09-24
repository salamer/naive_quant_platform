import pandas as pd
from sklearn import svm
import cPickle as pickle
from sklearn.externals import joblib
import os
import time
from db import training_result,trainning_state


def main(trainning_data, predict_data, target, col_name, task_name):

    train_X = trainning_data[col_name]
    predict_X = predict_data[col_name]
    train_Y = trainning_data[target]
    train_X = train_X.as_matrix()
    predict_X = predict_X.as_matrix()
    SVM(train_X, train_Y, predict_X, task_name)
    task = trainning_state.objects(taskName=task_name)
    task.state="OK"
    task.save()

def SVM(trainning_X, train_Y, predict_X, task_name):
    clf = svm.SVC(kernel="linear", C=0.025)
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res = res.tolist()
    tsk = training_result(
        task_name=task_name,
        clf_name="SVM",
        result=res,
    )
