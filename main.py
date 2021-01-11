import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotting

# defines which scaling method will be used
# and which classifier
# (this has to be down in the code as well!)
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression, LinearRegression

# define the column names and file addresses
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
training_set_address = 'training.csv'
testing_set_address = 'testing.csv'
# define for each name the class num in a dictionary
classes = {
    'Iris-setosa': 1,
    'Iris-versicolor': 2,
    'Iris-virginica': 3,
}
# create a swapped model for prediction naming
classesFromKeys = {
    value: key for key, value in classes.items()
}
# define the columns of features and the column of the classes
columnClass = 4
columnFeaturesStart, columnFeaturesStop = 0, 4  # column features stop is excluded, start is included!

# read the train, testing and cross validation csv
training = pd.read_csv(training_set_address, names=names)
testing = pd.read_csv(testing_set_address, names=names)

# plotting for data preview
plotting.plot(training, names[columnClass])

# slice the arrays: the data are in columns 0-4 (excl.)
# and the names (classes) in column 4
training_data = training.iloc[:, columnFeaturesStart:columnFeaturesStop].values

training_target_pre = training.iloc[:, columnClass].values
training_target = []

# class names in numbers
for name in training_target_pre:
    training_target.append(classes[name])

# do the same with the testing dataset
testing_data = testing.iloc[:, columnFeaturesStart:columnFeaturesStop].values

testing_target_pre = testing.iloc[:, columnClass].values
testing_target = []

for name in testing_target_pre:
    testing_target.append(classes[name])

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


# function for predicting (not used yet)
def predict(data):
    global scaling
    global model
    pre_predictions = model.predict(scaling.transform(data))
    predictions = []

    for prediction in pre_predictions:
        predictions.append(classesFromKeys[int(round(prediction))])

    return predictions
