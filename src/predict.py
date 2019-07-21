# Author: Nima Daryabar
"""
    Using Decision Tree Regression to predict band score from given scores.
"""
from sklearn import tree


def predict_score(scores_list, given_scores):
    # Training data for Decision Tree Regression
    X = []
    y = []
    for _, lst in enumerate(scores_list):
        # print(_ , lst)
        X.append(lst[0:4])
        y.append(lst[4])

    # Decision Tree Regression. tarining data set
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(X, y)
    # print(clf.predict([user_scores]))

    # Predicting the IELTS band score
    print()
    band_score = clf.predict([given_scores])
    print(f"result: {float(band_score)}")
    return band_score