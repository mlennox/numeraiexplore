import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from loader import load_training

training_data = load_training()


# Transform the loaded CSV data into numpy arrays
features = [feature for feature in list(training_data) if "feature" in feature]
X = training_data[features]

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

# # here we manually inspect the correlation plot and pull out highly correlated features, whether positive or negative
# # correlations = [34, 1, 44, 14, 33, 43, 15, 48, 21]
# correlations = [1, 14, 21, 33, 48]
# X_correlation = X.iloc[:, correlations]
# scatter_matrix(X_correlation)
# tick_marks = [i for i in range(len(X_correlation.columns))]
# plt.xticks(tick_marks, X_correlation.columns, rotation='vertical')
# plt.yticks(tick_marks, X_correlation.columns)
# plt.show()
