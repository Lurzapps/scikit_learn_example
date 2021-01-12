# define the column names, dataset address and class column index
class_column_index = 2
column_features_start, column_features_stop = 3, 10  # column features stop is excluded, start is included!

dataset_address = 'datasets/1.csv'
dataset_descriptor_address = 'datasets/1.txt'


def column_names() -> list:
    with open(dataset_descriptor_address, 'r') as f:
        return f.read().split(',')