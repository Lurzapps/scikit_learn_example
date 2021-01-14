from pandas import DataFrame
import pandas as pd

# define the column names, dataset address and class column index
class_column_index = 0
dataset_name = ['Delhi', 'London', 'Bangalore', 'Melbourne'][3]


# methods to get columns and dataset address
def dataset_address() -> str:
    global dataset_name
    return 'datasets/%s.csv' % dataset_name


def column_names() -> list:
    global dataset_name
    with open('datasets/%s.txt' % dataset_name, 'r') as f:
        return f.read().splitlines()[0].split(';')


def column_features_start_stop() -> tuple[int, int]:  # column features stop is excluded, start is included!
    global dataset_name
    with open('datasets/%s.txt' % dataset_name, 'r') as f:
        lines = f.read().splitlines()
        return int(lines[1]), int(lines[2])


def read_df() -> DataFrame:
    return pd.read_csv(dataset_address(), sep=';', quotechar='"', skipinitialspace=True, names=column_names())
