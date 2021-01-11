import pandas as pd

import utils
import global_variables as gl_vars


# defines which scaling method will be used
# and which classifier
# (this has to be down in the code as well!)
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression, LinearRegression

# read the train, testing and cross validation csv
training = pd.read_csv(gl_vars.training_set_address, names=gl_vars.column_names)
testing = pd.read_csv(gl_vars.testing_set_address, names=gl_vars.column_names)

# slice the arrays: the data are in columns 0-4 (excl.)
# and the names (classes) in column 4
training_data = training.iloc[:, gl_vars.column_features_start:gl_vars.column_features_stop].values

training_target_pre = training.iloc[:, gl_vars.class_column_index].values
training_target = []

# class names in numbers
for name in training_target_pre:
    training_target.append(gl_vars.classes[name])

# do the same with the testing dataset
testing_data = testing.iloc[:, gl_vars.column_features_start:gl_vars.column_features_stop].values

testing_target_pre = testing.iloc[:, gl_vars.class_column_index].values
testing_target = []

for name in testing_target_pre:
    testing_target.append(gl_vars.classes[name])

# init the scaler
scaling = MinMaxScaler()
# scale on axis the data, set the target
trainingX, trainingY = scaling.fit_transform(training_data), training_target

# the model model
model = LinearRegression()
# fit linear model
model.fit(trainingX, trainingY)

# fit the testing data
testingX = scaling.transform(testing_data)
# the testing y is the testing_target
# print the score of the testing data
print('score: %f' % model.score(testingX, testing_target))

# save the model afterwards
utils.save_model_and_scaling(model, scaling)
