import csv

import utils
import pandas as pd
import global_variables as gl_vars

# read csv
data = gl_vars.read_df()
# print the head of the csv
print(data.head())
# plot
utils.plot(data)
