import seaborn as sns
import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_lots


def create_plot(dataset, feature, era, filepath='images/violin/violinplot_era'):
    ax = sns.catplot(x="target_bernie", y="feature" + str(feature),
                     kind='violin', data=dataset)
    ax.set(ylim=(0.0, 1.0))
    plt.savefig(filepath + str(era) +
                '_feature' + str(feature) + '.png')


training_data = load_training()


for era in range(1, 5):
    X = pull_lots(training_data[training_data['era'] == 'era' + str(era)])
    for feature in range(1, 5):
        create_plot(X, feature, era)
