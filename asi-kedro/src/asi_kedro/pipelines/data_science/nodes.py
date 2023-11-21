"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
import numpy as np
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from autogluon.tabular import TabularPredictor
from autogluon.tabular import TabularDataset

def train_model(df: TabularDataset) -> LinearRegression:
    # Assuming the last column of df is 'target' and rest are features
    label_column = 'Potability'
    task = TabularPredictor(label=label_column, eval_metric='log_loss')
    predictor = task.fit(train_data=df,   
                     auto_stack=True,
                     verbosity=2)

    return predictor

def test_model(predictor: TabularPredictor, test_data: pd.DataFrame) -> DataFrame:
    
    # Return metrics in a dictionary
    return pd.DataFrame(predictor.predict_proba(test_data, as_pandas=True))

