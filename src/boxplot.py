import seaborn as sns
import matplotlib.pyplot as plt

from loader import load_training, pull_features, pull_lots

training_data = load_training()


#  , 'feature4',
#  'feature5', 'feature6', 'feature7', 'target_bernie']

# sns.pairplot(X[select_features].sample(
#     frac=1.0), aspect=1, hue='target_bernie')
# plt.savefig('images/scatter/scatter_matrix_seaborn_hue.png')


# sns.catplot(x="target_bernie", y="feature1",
#             kind='box', data=X[select_features])
# plt.savefig('images/scatter/boxplot_feature1.png')

# sns.catplot(x="target_bernie", y="feature2",
#             kind='box', data=X[select_features])
# plt.savefig('images/scatter/boxplot_feature2.png')

# sns.catplot(x="target_bernie", y="feature3",
#             kind='box', data=X[select_features])
# plt.savefig('images/scatter/boxplot_feature3.png')
