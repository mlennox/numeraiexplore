from loader import load_training, pull_features

X = pull_features(load_training())

print(X.describe())
