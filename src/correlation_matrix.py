import pandas as pd
import matplotlib.pyplot as plt

from loader import load_training, pull_features


def create_correlation_matrix(dataset, filename, filepath='images/correlation/', cmap=plt.cm.viridis):
    correlation = dataset.corr()
    fig, ax = plt.subplots()
    matrix = ax.imshow(correlation, cmap=cmap,
                       interpolation='nearest')
    fig.colorbar(matrix)
    tick_marks = [i for i in range(len(dataset.columns))]
    plt.xticks(tick_marks, dataset.columns, rotation='vertical')
    plt.yticks(tick_marks, dataset.columns)
    # now make the axes legible - we don't need them all
    for label in ax.xaxis.get_ticklabels()[1::2]:
        label.set_visible(False)
    for label in ax.yaxis.get_ticklabels()[1::2]:
        label.set_visible(False)
    plt.savefig(filepath + filename)
    plt.clf()


create_correlation_matrix(pull_features(
    load_training()), 'correlation_matrix_all_eras.png')
