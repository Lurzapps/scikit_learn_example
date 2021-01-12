# define the column names, dataset address and class column index
column_names = ['passenger id', 'survived', 'sex', 'age', 'fare', 'pclass_1', 'Pclass_2', 'Pclass_3', 'Family_size',
                'Title_1', 'Title_2', 'Title_3', 'Title_4', 'Emb_1', 'Emb_2', 'Emb_3']
class_column_index = 1
column_features_start, column_features_stop = 2, 9  # column features stop is excluded, start is included!

main_dataset_address = 'training.csv'
training_set_address = 'training.csv'
testing_set_address = 'testing.csv'

classes = {
    1: 1,
    0: 0
}
