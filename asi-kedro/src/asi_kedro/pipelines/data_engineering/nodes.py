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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from typing import Tuple


def data_loading(file):
    dataset = read_csv(file)
    #'../input/water_potability.csv'
    
def drop_na(df: DataFrame):
    return df.copy().dropna()


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

def show_null(dataset):
  missing_values = dataset.isnull().sum()
  num_rows, _ = dataset.shape

  plt.figure(figsize=(12, 6))
  sns.barplot(x=missing_values.values, y=missing_values.index, palette='viridis')
  plt.xlabel('Number of Missing Values')
  plt.title('Missing Values in DataFrame')
  plt.grid(axis='x', linestyle='--', alpha=0.7)
  plt.xlim(0, num_rows)

  for i, count in enumerate(missing_values):
    if(count == 0):
      continue
    plt.text(count + 10, i, str(count), va='center', fontsize=12)
  return plt

def split_data(data: DataFrame) -> Tuple[DataFrame, DataFrame]:
    train, test = train_test_split(data, test_size=0.2)  # Assuming a 80-20 split
    return train, test
    
    