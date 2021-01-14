from sys import argv

import global_variables as gl_vars
import seaborn as sns
import matplotlib.pyplot as plt

# show plot?
show = True

# set arguments in gl_vars if run with arguments
if len(argv) > 1:
    gl_vars.dataset_name = argv[1]
    show = not (argv[2] == '0')

# read csv
data = gl_vars.read_df()

# plot
# get columns to plot
# columns = []

# column_features_start, column_features_stop = gl_vars.column_features_start_stop()
# for i in range(len(data.columns)):
#     if i == gl_vars.class_column_index or column_features_start <= i < column_features_stop:
#         columns.append(data.columns[i])

print(data[data.columns])

# plot pairs
pair_plot = sns.pairplot(data[data.columns], height=1.8, aspect=1.8,
                         plot_kws=dict(edgecolor="k", linewidth=0.5),
                         diag_kind='kde')
# hue=gl_vars.column_names()[gl_vars.class_column_index]

# little design
fig = pair_plot.fig
fig.subplots_adjust(top=0.93, wspace=0.3)

# show the graph in sci view
if show:
    plt.show()
else:
    pair_plot.savefig('scores/%s.png' % gl_vars.dataset_name)


