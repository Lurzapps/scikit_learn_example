# this creates from a given dataset
# from random 75% of data a training dataset
# and from the rest 25% a testing dataset
import random
import os

# define the original file, the new testing and the new training file
og_addr = 'iris.csv'
testing_addr = 'testing.csv'
training_addr = 'training.csv'

# lists with training and testing lists
testing_list, training_list = [], []

# read the og file
with open(og_addr, 'r') as og:
    # read all lines
    for line in og.readlines():
        if random.uniform(0, 1) > 0.75:
            training_list.append(line)
        else:
            testing_list.append(line)

# delete the testing and training file if they already exist
if os.path.isfile(training_addr):
    os.remove(training_addr)
if os.path.isfile(testing_addr):
    os.remove(testing_addr)

# write these lists to the testing and training file
with open(training_addr, 'a') as training:
    for i in range(len(training_list)):
        training.write(training_list[i])

with open(testing_addr, 'a') as testing:
    for i in range(len(testing_list)):
        testing.write(testing_list[i])
