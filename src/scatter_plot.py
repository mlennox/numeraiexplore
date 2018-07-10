import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from loader import load_training, pull_features, pull_features_and_era_label

training_data = load_training()

# X_14 = pull_features_and_era_label(training_data, for_era='14')[
#     ['feature44_14', 'feature14_14']]
# X_33 = pull_features_and_era_label(training_data, for_era='33')[
#     ['feature44_33', 'feature14_33']]
# X_80 = pull_features_and_era_label(training_data, for_era='80')[
#     ['feature44_80', 'feature14_80']]

# scatter_data = pd.concat([X_14, X_33, X_80])

# ax14 = scatter_data.plot(kind='scatter', x='feature44_14',
#                          y='feature14_14', color='b')
# ax33 = scatter_data.plot(kind='scatter', x='feature44_33',
#                          y='feature14_33', color='r', ax=ax14)
# ax80 = scatter_data.plot(kind='scatter', x='feature44_80',
#                          y='feature14_80', color='y', ax=ax14)

# plt.show()


# X = pull_features(training_data, for_era=1)
# ax = X.plot(kind='scatter', x='feature14', y='feature44', color='r')
# plt.savefig('scatter/correlation_era1.png')

for era in range(1, 121):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    X = pull_features(training_data, for_era=era)
    X.plot(kind='scatter', x='feature14', y='feature44', color='r', ax=ax)
    plt.savefig('scatter/correlation_era' + str(era) + '.png')
    plt.close(fig)
