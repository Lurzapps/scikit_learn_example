# this creates from a given dataset
# from random 75% of data a training dataset
# and from the rest 25% a test dataset
import random
import os
import pandas as pd

# define the original file, the new test and the new train file
og_addr = 'iris.csv'
test_addr = 'test.csv'
train_addr = 'train.csv'

# lists with training and test lists
test_list, train_list = [], []

# read the og file
og = pd.read_csv(og_addr)

#
