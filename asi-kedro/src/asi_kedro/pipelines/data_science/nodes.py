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

def lr_train_model(df: pd.DataFrame) -> LinearRegression:
    # Assuming the last column of df is 'target' and rest are features
    X = df.iloc[:, :-1]
    y = df['Potability']

    model = LinearRegression()
    model.fit(X, y)

    return model

def lr_test_model(model: LinearRegression, df: pd.DataFrame) -> DataFrame:
    X = df.iloc[:, :-1]
    y_true = df['Potability']

    y_pred = model.predict(X)
    # vfunc = np.vectorize(lambda y: y < 0.5 if 0 else 1)
    # y_pred = vfunc(y_pred)

    # Calculate metrics
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    # Calculate "accuracy" based on epsilon threshold
    accurate_predictions = sum(abs(y_true - y_pred) <= 0.5)
    accuracy = accurate_predictions / len(y_true)
    print("accuracy: ", accuracy)

    # Return metrics in a dictionary
    return pd.DataFrame(
        {"y_true": y_true, "y_pred": y_pred}
    )

def rt_train_model(df: pd.DataFrame):
    X = df.loc[:, df.columns != 'Potability'].values
    y = df['Potability'].values

    model = RandomForestClassifier(n_estimators=250)
    model.fit(X, y)

    return model

def rt_test_model(model: RandomForestClassifier, df: pd.DataFrame) -> DataFrame:
    X = df.iloc[:, :-1]
    y_pred = model.predict(X)
    y_true = df['Potability']

    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    # Calculate "accuracy" based on epsilon threshold

    return pd.DataFrame(
        {"y_true": y_true, "y_pred": y_pred}
    )

