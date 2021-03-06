import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from loader import load_training, pull_features, pull_features_and_era_label

training_data = load_training()


def create_scatter_plot(dataset, featureX, featureY, filename, filepath='images/scatter/', color='red'):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    dataset.plot(kind='scatter', x=featureX, y=featureY, color=color, ax=ax)
    plt.savefig(filepath + filename)
    plt.close(fig)


# the correlated features
create_scatter_plot(pull_features(training_data), 'feature14',
                    'feature44', 'scatter_correlation_all_eras.png')
create_scatter_plot(pull_features(training_data, for_era=1),
                    'feature14', 'feature44', 'scatter_correlation_era1.png', color='orange')

# the independent features
create_scatter_plot(pull_features(training_data), 'feature2',
                    'feature40', 'scatter_independent_all_eras.png', color='deepskyblue')
create_scatter_plot(pull_features(training_data, for_era=1),
                    'feature2', 'feature40', 'scatter_independent_era1.png', color='mediumseagreen')
