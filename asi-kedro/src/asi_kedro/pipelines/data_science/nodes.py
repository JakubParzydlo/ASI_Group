"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
import numpy as np
import pandas as pd
from autogluon.tabular import TabularPredictor
from autogluon.tabular import TabularDataset

def train_model(train_data: TabularDataset) -> TabularPredictor:
    predictor = TabularPredictor(label='Potability', eval_metric='balanced_accuracy').fit(train_data=train_data)

    return predictor

def test_model(predictor: TabularPredictor, test_data: pd.DataFrame) -> pd.DataFrame:
    predictions = pd.DataFrame(predictor.predict(data=test_data, as_pandas=True))
    predictions.rename(columns={"Potability": "Prediction"}, inplace=True)
    predictions = pd.concat([predictions, test_data["Potability"]], axis=1)
    return predictions
