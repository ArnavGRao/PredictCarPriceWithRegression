import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.tree import DecisionTreeRegressor

import dataCleanup
import loadData
from custom_transformers import LogTransformer


def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())


train_set, test_set = loadData.partition_dataset()
car = train_set.drop("price", axis=1)
car_labels = train_set["price"].copy()

dataCleanup.feature_engineer(car)
# Create a single pipeline for all preprocessing
num_attribs = list(car.select_dtypes(include="number").columns)
cat_attribs = list(car.select_dtypes(include="object").columns)
log_attribs = ["horsepower", "enginesize"]
# Adjust num_attribs to not include log_attribs to avoid processing them twice
other_num_attribs = [col for col in num_attribs if col not in log_attribs]

full_pipeline = ColumnTransformer(
    [
        ("log", LogTransformer(log_attribs), log_attribs),
        ("robust", RobustScaler(), other_num_attribs),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_attribs),
    ]
)

car_prepared = full_pipeline.fit_transform(car)

"""
# Evaluate linear regression
print("--- Linear Regression ---")
lin_reg = LinearRegression()
lin_scores = cross_val_score(
    lin_reg, car_prepared, car_labels, scoring="neg_mean_squared_error", cv=10
)
lin_rmse_scores = np.sqrt(-lin_scores)
display_scores(lin_rmse_scores)


# Evaluate decision tree
print("\n--- Decision Tree ---")
tree_reg = DecisionTreeRegressor(random_state=42)
tree_scores = cross_val_score(
    tree_reg, car_prepared, car_labels, scoring="neg_mean_squared_error", cv=10
)
tree_rmse_scores = np.sqrt(-tree_scores)
display_scores(tree_rmse_scores)

# evaluate Random Forest
print("\n--- Random Forest ---")
forest_reg = RandomForestRegressor(random_state=42)
forest_scores = cross_val_score(
    forest_reg, car_prepared, car_labels, scoring="neg_mean_squared_error", cv=10
)
forest_rmse_scores = np.sqrt(-forest_scores)
display_scores(forest_rmse_scores)
"""

# Random forest perfomed best so hyper parameter tuning (grid search)

param_grid = [
    # try 12 (3x4) combinations of features
    {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8]},
    # then try 6 (2x3) combinations with bootstrap set to False
    {"bootstrap": [False], "n_estimators": [3, 10], "max_features": [2, 3, 4]},
]

forest_reg = RandomForestRegressor(random_state=42)
# train across 5 folds, that's a total of (12+6)*5=90 rounds of training
grid_search = GridSearchCV(
    forest_reg,
    param_grid,
    cv=5,
    scoring="neg_mean_squared_error",
    return_train_score=True,
)
grid_search.fit(car_prepared, car_labels)

print("Best parameters found: ", grid_search.best_params_)

# cross validating
final_model = grid_search.best_estimator_
final_scores = cross_val_score(
    final_model, car_prepared, car_labels, scoring="neg_mean_squared_error", cv=10
)
final_rmse_scores = np.sqrt(-final_scores)
display_scores(final_rmse_scores)

# calculating rmse
X_test = test_set.drop("price", axis=1)
y_test = test_set["price"].copy()
dataCleanup.feature_engineer(X_test)
X_test_prepared = full_pipeline.transform(X_test)

final_predictions = final_model.predict(X_test_prepared)
final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
print(f"\nFinal RMSE on Test Set: {final_rmse}")

# important features
feature_importances = final_model.feature_importances_
feature_names = full_pipeline.get_feature_names_out()
importances = sorted(zip(feature_importances, feature_names), reverse=True)

for importance, name in importances:
    print(f"{name}: {importance}")
