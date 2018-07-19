import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_lots

# selected_features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6',
#                      'feature7', 'feature8', 'feature9', 'feature10', 'feature11', 'feature12']


def create_histogram(dataset, selected_features, group):
    ax = (dataset[selected_features]).hist(ylabelsize=6, xlabelsize=5, bins=20)
    for axnext in ax:
        for x in axnext:
            x.spines['right'].set_visible(False)
            x.spines['top'].set_visible(False)
            x.spines['left'].set_visible(False)
            x.title.set_fontsize(7)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.savefig('images/other/histogram' + str(group) + '.png')


dataset = load_training()
for group in range(1, 50 - 9, 9):
    selected_features = ['feature' +
                         str(feature) for feature in range(group, group + 9)]
    create_histogram(dataset, selected_features, group)
