import seaborn as sns
import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_features_and_era_label

training_data = load_training()

X = pull_features(training_data, for_era=1)

sns.pairplot(X.sample(frac=1.0), aspect=1)
plt.savefig('images/scatter/scatter_matrix_seaborn.png')
