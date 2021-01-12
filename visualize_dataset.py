import csv

import utils
import pandas as pd
import global_variables as gl_vars

# read csv
data = pd.read_csv(gl_vars.dataset_address(), quotechar='"', skipinitialspace=True, names=gl_vars.column_names())
# plot
utils.plot(data)
