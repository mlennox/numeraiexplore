import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pandas.plotting import scatter_matrix

from loader import load_training, pull_features


def create_correlation_matrix(dataset, filename, cmap=plt.cm.viridis):
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
    plt.savefig(filename)
    plt.clf()


def calc_image_diff(imageA_filename, imageB_filename, diff_filename):
    imageA = mpimg.imread(imageA_filename)
    imageB = mpimg.imread(imageB_filename)
    diff_image = np.subtract(imageA[:, :, 1:4], imageB[:, :, 1:4])
    diff_image = np.subtract([1, 1, 1], diff_image)
    mpimg.imsave(diff_filename, diff_image)


def calc_mean_squared_diff(imageA_filename, imageB_filename):
    imageA = mpimg.imread(imageA_filename)
    imageB = mpimg.imread(imageB_filename)
    diff = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    diff /= float(imageA.shape[0] * imageA.shape[1])
    return diff


training_data = load_training()
negative = pull_features(training_data, target_bernie_value=0, for_era=1)
positive = pull_features(training_data, target_bernie_value=1, for_era=1)

create_correlation_matrix(positive, 'images/matrix_positive.png')

create_correlation_matrix(negative, 'images/matrix_negative.png')

calc_image_diff('images/matrix_positive.png',
                'images/matrix_negative.png', 'images/diff.png')

print('Mean squared difference', calc_mean_squared_diff(
    'images/matrix_positive.png', 'images/matrix_negative.png'))

# show image diff for all eras

create_correlation_matrix(pull_features(
    training_data, target_bernie_value=1), 'images/matrix_positive_all_eras.png')

create_correlation_matrix(pull_features(
    training_data, target_bernie_value=0), 'images/matrix_negative_all_eras.png')

calc_image_diff('images/matrix_positive_all_eras.png',
                'images/matrix_negative_all_eras.png', 'images/CorrelationDiff_all_aras.png')
