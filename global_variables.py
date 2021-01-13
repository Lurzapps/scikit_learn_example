from pandas import DataFrame
import pandas as pd

# define the column names, dataset address and class column index
class_column_index = 2
column_features_start, column_features_stop = 3, 10  # column features stop is excluded, start is included!
dataset_name = 'London'


# methods to get columns and dataset address
def dataset_address() -> str:
    global dataset_name
    return 'datasets/%s.csv' % dataset_name


def column_names() -> list:
    global dataset_name
    with open('datasets/%s.txt' % dataset_name, 'r') as f:
        return f.read().split(';')


def read_df() -> DataFrame:
    return pd.read_csv(dataset_address(), sep=';', quotechar='"', skipinitialspace=True, names=column_names())
