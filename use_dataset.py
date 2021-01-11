import utils
import global_variables as gl_vars

# read the model and scaling
model, scaling = utils.load_model_and_scaling()

# create a swapped model for prediction naming
classes_from_keys = {
    value: key for key, value in gl_vars.classes.items()
}


# define predict method to be used from console
def predict(data):
    global model
    global scaling
    utils.predict(classes_from_keys, model, scaling, data)
