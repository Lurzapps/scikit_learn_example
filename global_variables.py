

# define the column names, dataset address and class column index
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
class_column_index = 4
column_features_start, column_features_stop = 0, 4  # column features stop is excluded, start is included!

main_dataset_address = 'iris.csv'
training_set_address = 'training.csv'
testing_set_address = 'testing.csv'

classes = {
    'Iris-setosa': 1,
    'Iris-versicolor': 2,
    'Iris-virginica': 3,
}

