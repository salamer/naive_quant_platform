import pandas as pd
from sklearn import svm
import cPickle as pickle
from sklearn.externals import joblib
import os
import time
from state_db import State

clf = svm.SVC(kernel="linear", C=0.025)


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
