import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from picipixi import create_gif

from loader import load_training, pull_features, pull_features_and_era_label


def create_scatter_plot(dataset, filename, featureX='feature14', featureY='feature44',
                        filepath='images/scatter/animation/', color='red'):
    era_plot = dataset.plot(kind='scatter', x=featureX,
                            y=featureY, color=color)
    era_plot.set_ylim(0.0, 1.0)
    era_plot.set_xlim(0.0, 1.0)
    plt.savefig(filepath + filename)


training_data = load_training()


# create the animation frames
for era in range(1, 121):
    X = pull_features(training_data, for_era=era)
    create_scatter_plot(X, 'scatter_correlation_frame_era' + str(era) + '.png')

# TODO: combine the frames into an animation
# create_gif('images/scatter/scatter_correlation_all_eras.gif', 'images/scatter/animation', 'scatter_correlation_frame_era')
