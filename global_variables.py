# define the column names, dataset address and class column index
column_names = ['index', 'passenger id', 'survived', 'sex', 'age', 'fare', 'pclass_1', 'Pclass_2', 'Pclass_3', 'Family_size',
                'Title_1', 'Title_2', 'Title_3', 'Title_4', 'Emb_1', 'Emb_2', 'Emb_3']
class_column_index = 2
column_features_start, column_features_stop = 3, 10  # column features stop is excluded, start is included!

dataset_address = 'training.csv'
