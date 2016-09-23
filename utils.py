import pandas as pd

def open_data(filename):
    data = pd.read_csv(filename)
    return data
