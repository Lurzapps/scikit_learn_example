import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.base import ClassifierMixin, RegressorMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler

import global_variables as gl_vars


def save_model_and_scaling(model, scaling, idx):
    with open('models/model_%i.pkl' % idx, 'wb') as model_file:
        pickle.dump(model, model_file)
    with open('models/scaling_%i.pkl' % idx, 'wb') as scaling_file:
        pickle.dump(scaling, scaling_file)


def load_model_and_scaling(idx):
    with open('models/model_%i.pkl' % idx, 'rb') as model_file:
        model = pickle.load(model_file)
    with open('models/scaling_%i.pkl' % idx, 'rb') as scaling_file:
        scaling = pickle.load(scaling_file)
    return model, scaling


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start
