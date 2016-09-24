import pandas as pd
from sklearn import svm
import cPickle as pickle
from sklearn.externals import joblib
import os
import time
from db import training_result,trainning_state


def main(trainning_data, predict_data, target, col_name, task_name,stock_id):

    train_X = trainning_data[col_name]
    predict_X = predict_data[col_name]
    train_Y = trainning_data[target]
    train_X = train_X.as_matrix()
    predict_X = predict_X.as_matrix()
    SVM(train_X, train_Y, predict_X, task_name,predict_data,stock_id)
    task = trainning_state.objects(taskName=task_name).update_one(set__state="OK")

def SVM(trainning_X, train_Y, predict_X, task_name,origin_data,stock_id):
    clf = svm.SVC(kernel="linear", C=0.025)
    print trainning_X
    print train_Y
    print predict_X
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i]==1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="SVM",
        result=res_
    )
    tsk.save()
