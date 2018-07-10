import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from loader import load_training, pull_features

X = pull_features(load_training())

correlation = X.cov()
plt.imshow(correlation, cmap=plt.cm.viridis, interpolation='nearest')
plt.colorbar()
ax = plt.axes()
tick_marks = [i for i in range(len(X.columns))]
plt.xticks(tick_marks, X.columns, rotation='vertical')
plt.yticks(tick_marks, X.columns)
# now make the axes legible - we don't need them all
for label in ax.xaxis.get_ticklabels()[1::2]:
    label.set_visible(False)
for label in ax.yaxis.get_ticklabels()[1::2]:
    label.set_visible(False)
plt.show()
