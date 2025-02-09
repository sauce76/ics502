from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import Ridge
from skopt import BayesSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Load the California housing dataset
data = fetch_california_housing()
X = data.data
y = data.target  # This is a continuous target variable

# Display the first 10 rows of the DataFrame


# Split the data for outer cross-validation
outer_cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Hyperparameter search space for Ridge regression
param_space = {
    'alpha': (1e-6, 1e+6, 'log-uniform')  # Log scale for alpha (regularization)
}

# Store scores for the outer cross-validation
nested_scores = []

for train_idx, test_idx in outer_cv.split(X, y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # Inner cross-validation for hyperparameter tuning with BayesSearchCV
    bayes_search = BayesSearchCV(
        Ridge(),  # Ridge regression model
        param_space,  # Hyperparameter space
        n_iter=10,  # Number of iterations for Bayesian optimization
        cv=5,  # Inner CV for hyperparameter tuning
        scoring='neg_mean_squared_error',  # Use negative MSE for regression
        random_state=42
    )

    # Fit model on the training set and tune hyperparameters
    bayes_search.fit(X_train, y_train)

    # Evaluate on the outer test set
    y_pred = bayes_search.predict(X_test)
    score = mean_squared_error(y_test, y_pred)  # MSE for regression
    nested_scores.append(score)

# Calculate the average and standard deviation of the MSE from the outer CV
print(f'Average MSE: {np.mean(nested_scores)}')
print(f'Standard Deviation of MSE: {np.std(nested_scores)}')
