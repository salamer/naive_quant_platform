import pandas as pd
from sklearn import svm
import cPickle as pickle
from sklearn.externals import joblib
import os
import time
from db import training_result

clf = svm.SVC(kernel="linear", C=0.025)


def main(trainning_data,predict_data,target,useless_label,task_name):
    #process
    columns_name = trainning_data.columns
    columns_name.delete(useless_label)
    train_X=trainning_data[columns_name]
    predict_X=predict_data[columns_name]
    train_Y=trainning_data[target]
    train_X = train_X.as_matrix()
    predict_X = predict_X.as_matrix()
    pass


def SVM(trainning_X,train_Y,predict_X,task_name):
    clf = svm.SVC(kernel="linear", C=0.025)
    clf.fit(trainning_X,train_Y)
    res = clf.predict(predict_X)
    res = res.tolist()
    tsk = training_result(
        task_name = task_name,
        clf_name = "SVM",
        result = res,
    )




def open_data(filename):
    data = pd.read_csv(filename)
    return data


def train(data, uesless_label, target, filename):
    train_df = pd.DataFrame()
    for label in data.columns:
        if label not in uesless_label:
            data[label] = data[label].fillna(data[label].min())
            data[label].apply(lambda x: (x - data[label].min()) /
                              (data[label].max() - data[label].min()))
            train_df = train_df.append(data[label])
    train_df = train_df.T
    target = data[target]
    train_matrix = train_df.as_matrix()
    clf.fit(train_matrix, target)
    path = "clf/" + filename + str(time.time()) + ".pkl"
    with open(path, 'wb') as fid:
        pickle.dump(clf, fid)
#    state = State.objects(name=filename)[0]
#    state.state = "ok"
#    state.clfPath = path
