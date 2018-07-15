import pandas as pd


def load_training():
    return pd.read_csv(
        './data/numerai_training_data.csv', header=0)


def load_tournament():
    return pd.read_csv(
        './data/numerai_tournament_data.csv', header=0)


def pull_features(data_source, for_era=None, target_bernie_value=None):
    if for_era is not None:
        dataset = data_source[data_source['era'] == 'era' + str(for_era)]
    else:
        dataset = data_source
    if target_bernie_value is not None:
        dataset = dataset[dataset['target_bernie'] == target_bernie_value]
    # print(dataset.describe())
    features = [feature for feature in list(dataset) if "feature" in feature]
    return dataset[features]


def pull_features_and_era_label(data_source, for_era):
    # if for_era = 12 the data will pull onlu rows with 'era' column matching 'era12'
    # and the returned dataframe will have labels suffixed with era 'feature23_12'
    dataset = pull_features(data_source, for_era)
    features = [feature for feature in list(dataset) if "feature" in feature]
    features_suffixed = [f + '_' + for_era for f in features]
    # print('SUFFIXED', features_suffixed)
    updated_columns = dict(zip(features, features_suffixed))
    print('UPDATED COLUMNS', updated_columns)
    dataset.rename(columns=updated_columns, inplace=True)
    return dataset
