import seaborn as sns
import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_lots

training_data = load_training()


for era in range(1, 5):
    X = pull_lots(training_data[training_data['era'] == 'era' + str(era)])
    for feature in range(1, 5):
        sns.catplot(x="target_bernie", y="feature" + str(feature),
                    kind='violin', data=X)
        plt.savefig('images/violin/violinplot_era' + str(era) +
                    '_feature' + str(feature) + '.png')
