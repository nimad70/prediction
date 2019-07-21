# Author: Nima Daryabar
"""
    Using Decision Tree Regression to predict band score from given scores.
"""

def predict_score(scores_list, given_scores):
    # Training data for Decision Tree Regression
    X = []
    y = []
    for _, lst in enumerate(ielts_scores_list):
        # print(_ , lst)
        X.append(lst[0:4])
        y.append(lst[4])

    # Decision Tree Regression. tarining data set
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(X, y)