from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


def exec(df):
    values = df.values
    X = values[:, 0:9]
    y = values[:, 9]

    model = LinearDiscriminantAnalysis()
    cv = KFold(n_splits=3, shuffle=True, random_state=1)

    result = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

    return result