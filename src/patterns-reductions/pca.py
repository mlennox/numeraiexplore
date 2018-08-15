# https://alex.dzyoba.com/blog/python-import/
import sys

sys.path.append("..")

from sklearn.decomposition import PCA
from core.loader import load_training

# , pull_features, pull_lots

dataset = load_training()
