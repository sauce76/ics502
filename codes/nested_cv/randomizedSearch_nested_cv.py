import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, RandomizedSearchCV
from sklearn.linear_model import Ridge
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error
from scipy.stats import uniform

# Load California housing dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Define number of folds for nested CV
outer_cv = KFold(n_splits=5, shuffle=True, random_state=42)
inner_cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Define hyperparameter search space for Ridge Regression
param_dist = {"alpha": uniform(0.01, 100)}  # Randomly samples alpha from [0.01, 100]

# Store outer loop results
nested_mse_scores = []

# Outer CV loop
for train_idx, test_idx in outer_cv.split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # Inner CV: Hyperparameter tuning with randomized search
    ridge = Ridge()
    random_search = RandomizedSearchCV(
        ridge, param_distributions=param_dist, n_iter=10, cv=inner_cv,
        scoring='neg_mean_squared_error', random_state=42, n_jobs=-1
    )
    random_search.fit(X_train, y_train)

    # Best model from inner CV
    best_model = random_search.best_estimator_

    # Evaluate on the outer test set
    y_pred = best_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    nested_mse_scores.append(mse)

# Convert results to numpy array
nested_mse_scores = np.array(nested_mse_scores)

# Print results
print(f"Nested CV MSE (Mean): {nested_mse_scores.mean():.4f}")
print(f"Nested CV MSE (Std Dev): {nested_mse_scores.std():.4f}")
# Plot MSE distribution across outer folds
plt.boxplot(nested_mse_scores)
plt.xlabel("MSE")
plt.title("Nested Cross-Validation MSE Distribution")
plt.show()
