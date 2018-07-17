import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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


def calc_image_diff(imageA_filename, imageB_filename, diff_filename, filepath='images/correlation/'):
    # subtract the colour value of one image from the other
    imageA = mpimg.imread(filepath + imageA_filename)
    imageB = mpimg.imread(filepath + imageB_filename)
    # subtract the colour values of one image from the other on a pixel-by-pixel basis
    diff_image = np.subtract(imageA[:, :, 1:4], imageB[:, :, 1:4])
    # now invert the image difference - easier to see differences
    diff_image = np.subtract([1, 1, 1], diff_image)
    mpimg.imsave(filepath + diff_filename, diff_image)


def calc_mean_squared_diff(imageA_filename, imageB_filename, filepath='images/correlation/'):
    # calculate the mean-square difference between two images over all the pixels in an image
    imageA = mpimg.imread(filepath + imageA_filename)
    imageB = mpimg.imread(filepath + imageB_filename)
    diff = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    diff /= float(imageA.shape[0] * imageA.shape[1])
    return diff


training_data = load_training()
negative = pull_features(training_data, target_bernie_value=0, for_era=1)
positive = pull_features(training_data, target_bernie_value=1, for_era=1)

create_correlation_matrix(positive, 'correlation_matrix_positive.png')

create_correlation_matrix(negative, 'correlation_matrix_negative.png')

calc_image_diff('correlation_matrix_positive.png', 'correlation_matrix_negative.png',
                'correlation_diff_era1.png')

print('Mean squared difference', calc_mean_squared_diff(
    'correlation_matrix_positive.png', 'correlation_matrix_negative.png'))

# show image diff for all eras

create_correlation_matrix(pull_features(
    training_data, target_bernie_value=1), 'correlation_matrix_positive_all_eras.png')

create_correlation_matrix(pull_features(
    training_data, target_bernie_value=0), 'correlation_matrix_negative_all_eras.png')

calc_image_diff('correlation_matrix_positive_all_eras.png',
                'correlation_matrix_negative_all_eras.png', 'correlation_diff_all_eras.png')
