import random
import os

import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

# defines which scaling method will be used
# and which classifier
# (this has to be down in the code as well!)
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

# define the column names and file addresses
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
enroll_set_address = 'enroll.csv'
test_set_address = 'test.csv'
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

# read the train, test and cross validation csv
enroll = pd.read_csv(enroll_set_address, names=names)
test = pd.read_csv(test_set_address, names=names)

# plotting for data preview
# get columns to plot
columns = enroll.columns.drop(['class'])
# create x data
x_data = range(0, enroll.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, enroll[column], label=column)
# set title and legend
ax.set_title('Iris Dataset')
ax.legend()

# show the graph in sci view
plt.show()

# slice the arrays: the data are in columns 0-4 (excl.)
# and the names (classes) in column 4
enroll_data = enroll.iloc[:, columnFeaturesStart:columnFeaturesStop].values

enroll_target_pre = enroll.iloc[:, columnClass].values
enroll_target = []

# class names in numbers
for name in enroll_target_pre:
    enroll_target.append(classes[name])

# do the same with the test dataset
test_data = test.iloc[:, columnFeaturesStart:columnFeaturesStop].values

test_target_pre = test.iloc[:, columnClass].values
test_target = []

for name in test_target_pre:
    test_target.append(classes[name])

# init the scaler
scaling = MinMaxScaler()
# scale on axis the data, set the target
enrollX, enrollY = scaling.fit_transform(enroll_data), enroll_target

# linear regression model
lin_reg = LinearRegression()
# fit linear model
lin_reg.fit(enrollX, enrollY)

# fit the test data
testX = scaling.transform(test_data)
# the test y is the test_target
# print the score of the test data
print('score: %f' % lin_reg.score(testX, test_target))


# function for predicting
def predict(data):
    global scaling
    global lin_reg
    pre_predictions = lin_reg.predict(scaling.transform(data))
    predictions = []

    for prediction in pre_predictions:
        predictions.append(classesFromKeys[int(round(prediction))])

    return predictions
