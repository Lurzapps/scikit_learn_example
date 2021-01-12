import os
import pandas as pd

import utils
import global_variables as gl_vars

# read
data = pd.read_csv('dataset.csv', quotechar='"', skipinitialspace=True, names=gl_vars.column_names())

# clean here

# save again
data.to_csv('dataset.csv', mode='w', index=False)
