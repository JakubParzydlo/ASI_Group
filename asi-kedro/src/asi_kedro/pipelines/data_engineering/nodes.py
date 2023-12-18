"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""
from sklearn.impute import KNNImputer
from pandas import read_csv
from pandas import DataFrame
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from typing import Tuple
from autogluon.tabular import TabularPredictor as task
from autogluon.tabular import TabularDataset


def data_loading(file):
    dataset = read_csv(file)
    #'../input/water_potability.csv'

def split_data(data: DataFrame) -> Tuple[DataFrame, DataFrame]:
    # test_size powinien być zmienialny przy użyciu argumentu z linii komend
    train, test = train_test_split(data, test_size=0.2)  # Assuming a 80-20 split
    train = TabularDataset(train)
    test = TabularDataset(test)
    return train, test
    
    