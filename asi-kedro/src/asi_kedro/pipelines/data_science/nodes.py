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
    predictor = TabularPredictor(label='Potability').fit(train_data=df)

    return predictor

def test_model(predictor: TabularPredictor, test_data: pd.DataFrame) -> DataFrame:
    predictions = pd.DataFrame(predictor.predict(data=test_data, as_pandas=True))
    predictions.rename(columns={"Potability": "Prediction"}, inplace=True)
    predictions = pd.concat([predictions, test_data["Potability"]], axis=1)
    return predictions
