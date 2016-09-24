import pandas as pd
import logging


def open_data(filename):
    data = pd.read_csv(filename)
    return data


def check_colums(col1, col2):
    for item in col1:
        if item not in col2:
            return False
    return True
