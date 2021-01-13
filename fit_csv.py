import os
import pandas as pd

import utils
import global_variables as gl_vars

file = 'datasets/London.csv'

# read
data = pd.read_csv(file, sep=';', quotechar='"', skipinitialspace=True, names=gl_vars.column_names())

# clean here
del data['idx']

# save again
data.to_csv(file, mode='w', index=False)
