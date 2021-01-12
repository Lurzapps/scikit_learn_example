import os
import pandas as pd

import utils
import global_variables as gl_vars

out = []

data = pd.read_csv('spotify_clean.csv', quotechar='"', skipinitialspace=True)
data.columns = gl_vars.column_names

for item in data['artists']:
    print(item)

data.to_csv('spotify_clean.csv', mode='w', index=False)
