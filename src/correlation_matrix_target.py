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
    print(type(imageA))
    print(imageA.shape)
    # print(imageA[:, :, 1])

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    print('Mean squared error', err)
    print(imageA[:, :, 1].shape)
    diff_image = np.subtract(imageA[:, :, 1], imageB[:, :, 1])
    # diff_image = np.subtract(imageA, imageB)
    print(diff_image)
    mpimg.imsave(diff_filename, diff_image)


training_data = load_training()
negative = pull_features(training_data, target_bernie_value=0, for_era=1)
positive = pull_features(training_data, target_bernie_value=1, for_era=1)

create_correlation_matrix(positive, 'images/matrix_positive.png')

create_correlation_matrix(negative, 'images/matrix_negative.png')

calc_image_diff('images/matrix_positive.png',
                'images/matrix_negative.png', 'images/diff.png')
