import utils
from sklearn.ensemble import RandomForestClassifier
import global_variables as gl_vars

idx = 0

# read the model and scaling
model, scaling = utils.load_model_and_scaling(idx)


# define predict method to be used from console
def predict(data):
    global model
    global scaling
    return model.predict(scaling.transform(data))
