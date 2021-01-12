import pandas as pd

import utils
import global_variables as gl_vars
import numpy as np

# defines which scaling method will be used
# and which classifier
# (this has to be down in the code as well!)
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import KFold

# read the dataset
df = pd.read_csv(gl_vars.dataset_address(), quotechar='"', skipinitialspace=True, names=gl_vars.column_names())

# create a kfold instance for cross validation
kfold = KFold(n_splits=5, shuffle=True)

# index for loop
idx = 0

# create splits form the dataframe
for train_df, test_df in kfold.split(df):
    # gather target and training data from data
    training_data = train_df.iloc[:, gl_vars.column_features_start:gl_vars.column_features_stop].values
    training_target = train_df.iloc[:, gl_vars.class_column_index].values

    # same for for testing split set
    testing_data = train_df.iloc[:, gl_vars.column_features_start:gl_vars.column_features_stop].values
    testing_target = train_df.iloc[:, gl_vars.class_column_index].values

    # init the scaler
    scaling = MinMaxScaler()
    # scale on axis the data, set the target
    trainingX, trainingY = scaling.fit_transform(training_data), training_target

    # the model model
    model = LogisticRegression()
    # fit linear model
    model.fit(trainingX, trainingY)

    # fit the testing data
    testingX = scaling.transform(testing_data)
    # the testing y is the testing_target
    # print the score of the testing data
    print('score %i: %f' % (idx, model.score(testingX, testing_target)))

    # save the model afterwards
    utils.save_model_and_scaling(model, scaling, idx)

    # grow idx
    idx += 1
