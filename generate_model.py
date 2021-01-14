import os
from sys import argv

import global_variables as gl_vars
import numpy as np
import utils

# defines which scaling method will be used
# and which classifier
# (this has to be down in the code as well!)
from sklearn.preprocessing import MinMaxScaler

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import KFold

# set arguments in gl_vars if run with arguments
if len(argv) > 1:
    gl_vars.dataset_name = argv[1]
    gl_vars.regressor_type = argv[2]
    gl_vars.save_models = not (argv[3] == '0')

# read the dataset
df = gl_vars.read_df()

# create a kfold instance for cross validation
kfold = KFold(n_splits=5, shuffle=True)

# index for loop
idx = 0

score = []

column_features_start, column_features_stop = gl_vars.column_features_start_stop()

with open('scores/%s_%s.txt' % (gl_vars.dataset_name, gl_vars.regressor_type), 'a') as logfile:
    with open('scores/all.txt', 'a') as all_logfile:
        # write header in file
        header = '%s | %s\n' % (gl_vars.dataset_name, gl_vars.regressor_type)
        logfile.write(header)
        all_logfile.write('\n\n' + header)

        # function for logging to file and console
        def log(a: str):
            print(a)
            logfile.write('\n' + a)
            all_logfile.write('\n' + a)


        # create splits form the dataframe
        for train_df_idx, test_df_idx in kfold.split(df):
            # create dataframes from split indices
            train_df = df.iloc[train_df_idx]
            test_df = df.iloc[test_df_idx]

            # gather target and training data from data
            training_data = train_df.iloc[:, column_features_start:column_features_stop].values
            training_target = train_df.iloc[:, gl_vars.class_column_index].values

            # same for for testing split set
            testing_data = train_df.iloc[:, column_features_start:column_features_stop].values
            testing_target = train_df.iloc[:, gl_vars.class_column_index].values

            # init the scaler
            scaling = MinMaxScaler()
            # scale on axis the data, set the target
            trainingX, trainingY = scaling.fit_transform(training_data), training_target

            # the model from name
            model = None
            if gl_vars.regressor_type == 'linear':
                model = LinearRegression()
            elif gl_vars.regressor_type == 'random-forest':
                model = RandomForestRegressor()
            elif gl_vars.regressor_type == 'k-nearest-neighbour':
                model = KNeighborsRegressor()

            # fit linear model
            model.fit(trainingX, trainingY)

            # fit the testing data
            testingX = scaling.transform(testing_data)
            # the testing y is the testing_target
            # print the score of the testing data
            # ! this is the score and not the error !
            this_score = model.score(testingX, testing_target)
            log('score %i: %f' % (idx, this_score))

            # save the model afterwards
            if gl_vars.save_models:
                utils.save_model_and_scaling(model, scaling, idx)

            # grow idx
            idx += 1

            # grow err
            score.append(this_score)

        # print median error
        arr = np.array(score)
        log('\n mean score: %f' % np.mean(arr))
        log(' median score: %f' % np.median(arr))
