import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import global_variables as gl_vars


def plot(data):
    # get columns to plot
    columns = []
    for i in range(len(data.columns)):
        if i == gl_vars.class_column_index or gl_vars.column_features_start <= i < gl_vars.column_features_stop:
            columns.append(data.columns[i])

    print(data[columns])

    # plot pairs
    pair_plot = sns.pairplot(data[columns], height=1.8, aspect=1.8,
                             plot_kws=dict(edgecolor="k", linewidth=0.5),
                             diag_kind='kde', hue=gl_vars.column_names[gl_vars.class_column_index])

    # little design
    pp_fig = pair_plot.fig
    pp_fig.subplots_adjust(top=0.93, wspace=0.3)

    # show the graph in sci view
    plt.show()


def save_model_and_scaling(model, scaling):
    with open('model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    with open('scaling.pkl', 'wb') as scaling_file:
        pickle.dump(scaling, scaling_file)


def load_model_and_scaling():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('scaling.pkl', 'rb') as scaling_file:
        scaling = pickle.load(scaling_file)
    return model, scaling


def predict(classes_from_keys, model, scaling, data):
    pre_predictions = model.predict(scaling.transform(data))
    predictions = []

    for prediction in pre_predictions:
        predictions.append(classes_from_keys[int(round(prediction))])

    return predictions


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
