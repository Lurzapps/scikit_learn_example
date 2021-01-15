import sys

import global_variables as gl_vars
import os

# delete old files in score dir
for f in os.listdir('scores'):
    os.remove(os.path.join('scores', f))

# set save models false
gl_vars.save_models = False

# loop through all cities and regressors and change gl_vars accordingly
# then run the generate_model.py file
for city in gl_vars.cities:
    gl_vars.dataset_name = city

    # draw the model
    os.system('visualize_dataset.py %s 0' % city)

    for regressor in gl_vars.regressors:
        gl_vars.regressor_type = regressor

        os.system('generate_model.py %s %s %s' % (city, regressor, '0'))

