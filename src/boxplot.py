import seaborn as sns
import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_lots

training_data = load_training()


for era in range(1, 5):
    X = pull_lots(training_data[training_data['era'] == 'era' + str(era)])
    for feature in range(1, 5):
        ax = sns.catplot(x="target_bernie", y="feature" + str(feature),
                         kind='box', data=X)
        ax.set(ylim=(0.0, 1.0))
        plt.savefig('images/box/boxplot_era' + str(era) +
                    '_feature' + str(feature) + '.png')
