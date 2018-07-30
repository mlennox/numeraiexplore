import seaborn as sns
import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_lots

training_data = load_training()

dataset = pull_lots(training_data[training_data["era"] == "era1"])

sns.pairplot(dataset, aspect=1)
plt.savefig("images/scatter/scatter_matrix_seaborn.png")

sns.pairplot(dataset, aspect=1, hue="target_bernie")
plt.savefig("images/scatter/scatter_matrix_seaborn_hue.png")

