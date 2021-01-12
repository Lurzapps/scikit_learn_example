# define the column names, dataset address and class column index
column_names = ['genres', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness',
                'liveness', 'loudness', 'speechiness', 'tempo', 'valence']
class_column_index = 0
column_features_start, column_features_stop = 1, 11  # column features stop is excluded, start is included!

main_dataset_address = 'spotify_clean.csv'
training_set_address = 'training.csv'
testing_set_address = 'testing.csv'

classes = {
    'acousticness': 1,
    'danceability': 2,
    'duration_ms': 3,
    'energy': 4,
    'instrumentalness': 5,
    'liveness': 6,
    'loudness': 7,
    'speechiness': 8,
    'tempo': 9,
    'valence': 10,
}
