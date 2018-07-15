import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from loader import load_training, pull_features, pull_features_and_era_label


def create_scatter_matrix(dataset, filename, color='red'):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    scatter_matrix(dataset, color=color, ax=ax)
    plt.savefig(filename)
    plt.close(fig)


training_data = load_training()

features_era1 = pull_features(training_data, for_era=1)
select_features = ['feature' + str(feature) for feature in range(10, 20)]
frac = 1.0
create_scatter_matrix(features_era1[select_features].sample(
    frac=frac), 'scatter/scatter_matrix.png')
