import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

from loader import load_training, pull_features, pull_lots

training_data = load_training()
X = pull_lots(training_data[training_data['era'] == 'era1'])
X.drop(columns=['era'], inplace=True)

parallel_coordinates(X[['feature1', 'feature14', 'feature4',
                        'feature43', 'target_bernie']], 'target_bernie')
plt.savefig('images/other/parallel.png')
