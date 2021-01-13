import csv

import utils
import pandas as pd
import global_variables as gl_vars

# read csv
data = gl_vars.read_df()
# plot
utils.plot(data)
