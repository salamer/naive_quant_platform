import pandas as pd
from sklearn import svm
import cPickle as pickle
from sklearn.externals import joblib
import os
import time
from db import training_result, trainning_state
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


def main(trainning_data, predict_data, target, col_name, task_name, stock_id):

    train_X = trainning_data[col_name]
    predict_X = predict_data[col_name]
    train_Y = trainning_data[target]
    train_X = train_X.as_matrix()
    predict_X = predict_X.as_matrix()
    SVM(train_X, train_Y, predict_X, task_name, predict_data, stock_id)
    SVC(train_X, train_Y, predict_X, task_name, predict_data, stock_id)
    KNN(train_X, train_Y, predict_X, task_name, predict_data, stock_id)
    DecisionTree(train_X, train_Y, predict_X,
                 task_name, predict_data, stock_id)
    RandomForest(train_X, train_Y, predict_X,
                 task_name, predict_data, stock_id)
    adaboost(train_X, train_Y, predict_X, task_name, predict_data, stock_id)
    Gaussian(train_X, train_Y, predict_X, task_name, predict_data, stock_id)
    LinearDiscriminant(train_X, train_Y, predict_X,
                       task_name, predict_data, stock_id)

    task = trainning_state.objects(
        taskName=task_name).update_one(set__state="OK")


def SVM(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = svm.SVC(kernel="linear", C=0.025)
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="linear SVM",
        result=res_
    )
    tsk.save()


def SVC(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = svm.SVC(gamma=2, C=1)
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="RBF SVM",
        result=res_
    )
    tsk.save()


def KNN(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = KNeighborsClassifier(5)
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="KNN(5)",
        result=res_
    )
    tsk.save()


def DecisionTree(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = DecisionTreeClassifier(max_depth=5)
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="Decision Tree",
        result=res_
    )
    tsk.save()


def RandomForest(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="Random Forest",
        result=res_
    )
    tsk.save()


def adaboost(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = AdaBoostClassifier()
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="adaboost",
        result=res_
    )
    tsk.save()


def Gaussian(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = GaussianNB()
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="GaussianNB",
        result=res_
    )
    tsk.save()


def Gaussian(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = GaussianNB()
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="GaussianNB",
        result=res_
    )
    tsk.save()


def LinearDiscriminant(trainning_X, train_Y, predict_X, task_name, origin_data, stock_id):
    clf = LinearDiscriminantAnalysis()
    clf.fit(trainning_X, train_Y)
    res = clf.predict(predict_X)
    res_ = []
    for i in range(len(res)):
        if res[i] == 1:
            res_.append(origin_data[stock_id][i])
    tsk = training_result(
        taskName=task_name,
        clf_name="Linear Discriminant Analysis",
        result=res_
    )
    tsk.save()
