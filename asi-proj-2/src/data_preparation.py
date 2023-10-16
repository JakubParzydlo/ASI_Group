import src.data_loading as dl
from sklearn.impute import KNNImputer
from pandas import DataFrame
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def drop_na():
    return dl.dataset.copy().dropna()


def avg_filling(dataset):
    # Calculate the average for each colum
    column_averages = dataset.mean()

    # Fill missing values in each column with its corresponding average
    df_filled = dataset.fillna(column_averages)

    return df_filled

def knn_filling(dataset):
    imputer = KNNImputer(n_neighbors=4, weights="uniform")

    dataset_knn = DataFrame(imputer.fit_transform(dataset))

    dataset_knn.columns = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon',
                           'Trihalomethanes', 'Turbidity', 'Potability']

    return dataset_knn

def iter_filling(dataset):
    imp = IterativeImputer(max_iter=25, random_state=0)
    dataset_iter = DataFrame(imp.fit_transform(dataset))
    dataset_iter.columns = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon',
                            'Trihalomethanes', 'Turbidity', 'Potability']

    return dataset_iter