"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

def train_model(df):
    model = LinearDiscriminantAnalysis()
    cv = KFold(n_splits=3, shuffle=True, random_state=1)

    return cv