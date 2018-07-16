import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from loader import load_training, pull_features, pull_features_and_era_label


def update_figure(matrix_fig):
    # rotate x-axis labels 45 degrees and y-axis to horizontal
    matrix_fig.xaxis.label.set_rotation(45)
    matrix_fig.yaxis.label.set_rotation(0)
    matrix_fig.get_yaxis().set_label_coords(-0.6, 0.5)
    # switch off ticks
    matrix_fig.set_xticks(())
    matrix_fig.set_yticks(())


def create_scatter_matrix(dataset, filename, color='red'):
    fig, ax = plt.subplots()
    matrix = scatter_matrix(dataset, color=color, ax=ax)
    [update_figure(m) for m in matrix.reshape(-1)]
    plt.savefig(filename)
    plt.close(fig)


def scatter_matrix_variation(dataset, select_features, filename_suffix='', frac=0.1):
    frac = 0.5
    create_scatter_matrix(dataset[select_features].sample(
        frac=frac), 'scatter/scatter_matrix' + filename_suffix + '.png')


training_data = load_training()

# scatter_matrix_variation(
#     pull_features(training_data, for_era=1),
#     ['feature' + str(feature) for feature in range(1, 50)],
#     '_era1_1_50',
#     frac=0.1)

scatter_matrix_variation(
    pull_features(training_data, target_bernie_value=0, for_era=1),
    ['feature4', 'feature5', 'feature6', 'feature14',
        'feature15', 'feature16', 'feature17'],
    # ['feature' + str(feature) for feature in range(4, 17)],
    '_era1_4_17',
    frac=1.0)
