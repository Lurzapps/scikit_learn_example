import matplotlib.pyplot as plt
import seaborn as sns


def plot(data, class_column_name):
    # get columns to plot
    columns = data.columns

    # plot pairs
    pair_plot = sns.pairplot(data[columns], height=1.8, aspect=1.8,
                             plot_kws=dict(edgecolor="k", linewidth=0.5),
                             diag_kind='kde', hue=class_column_name)

    # little design
    pp_fig = pair_plot.fig
    pp_fig.subplots_adjust(top=0.93, wspace=0.3)

    # show the graph in sci view
    plt.show()
