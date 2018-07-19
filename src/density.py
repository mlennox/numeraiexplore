import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_lots


def simplify_figs(ax):
    for axnext in ax:
        for x in axnext:
            x.spines['right'].set_visible(False)
            x.spines['top'].set_visible(False)
            x.spines['left'].set_visible(False)
            x.title.set_fontsize(7)
    plt.subplots_adjust(hspace=0.5)


def create_density(dataset, selected_features, group):
    ax = dataset[selected_features].plot(kind='density', subplots=True,
                                         layout=(3, 1), sharex=False, xlim=[0.0, 1.0])
    simplify_figs(ax)
    plt.savefig('images/other/density' + str(group) + '.png')


dataset = load_training()
for group in range(1, 50 - 3, 3):
    selected_features = ['feature' +
                         str(feature) for feature in range(group, group + 3)]
    create_density(dataset, selected_features, group)
