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
from autogluon import TabularPrediction as task

def train_model(df: task.Dataset) -> LinearRegression:
    # Assuming the last column of df is 'target' and rest are features
    predictor = task.fit(train_data=df, 
                     label='Potability',  
                     eval_metric='log_loss', 
                     auto_stack=True,
                     verbosity=2,
                     visualizer='tensorboard')

    return predictor

def test_model(model: task, df: pd.DataFrame) -> DataFrame:
    
    # Return metrics in a dictionary
    return pd.DataFrame(
        pred_probablities = predictor.predict_proba(test_data, as_pandas=True)
        return pred_probablities
    )

