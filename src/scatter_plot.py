import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from loader import load_training, pull_features, pull_features_and_era_label

training_data = load_training()


def create_scatter_plot(dataset, featureX, featureY, filename):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    dataset.plot(kind='scatter', x=featureX, y=featureY, color='r', ax=ax)
    plt.savefig(filename)
    plt.close(fig)


create_scatter_plot(pull_features(training_data), 'feature14',
                    'feature44', 'scatter/ScatterCorrelation.png')
create_scatter_plot(pull_features(training_data, for_era=1),
                    'feature14', 'feature44', 'scatter/Era1ScatterCorrelation.png')
