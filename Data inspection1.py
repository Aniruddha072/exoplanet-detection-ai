import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# loading the local csv file
base_dir = Path(__file__).resolve().parent.parent
train_data = pd.read_csv(base_dir / "data" / "exoTrain.csv")
test_data = pd.read_csv(base_dir / "data" / "exoTest.csv")

# Check the dimensions of the matrix

print(f"Train data shape: {train_data.shape}")
print(f"Test data shape: {test_data.shape}")

# 1. Extract the labels (the first column)
y_train_raw = train_data.iloc[:, 0].values
y_test_raw = test_data.iloc[:, 0].values

# 2. Convert Kaggle labels (2 -> 1 for planet, 1 -> 0 for no planet)
y_train = np.where(y_train_raw == 2, 1, 0)
y_test = np.where(y_test_raw == 2, 1, 0)

# 3. Extract just the raw light curve data (drop the label column)
X_train = train_data.iloc[:, 1:].values
X_test = test_data.iloc[:, 1:].values

# Quick sanity check: How many planets do we actually have?
print(f"Number of confirmed planet stars in training set: {np.sum(y_train)}")
print(f"Number of normal stars in training set: {len(y_train) - np.sum(y_train)}")


# Find the index of the first non-planet star (where y_train == 0)
non_planet_indices = np.where(y_train == 0)[0]
first_non_planet_idx = non_planet_indices[0]

# plot the first non-planet star
plt.figure(figsize=(14, 4))
plt.plot(X_train[first_non_planet_idx], color='crimson', lw=0.5)
plt.title(f"Non-Planet/False Positive light curve - Star index {first_non_planet_idx}", fontsize=14)
plt.xlabel("Time(sequential observations)", fontsize=12)
plt.ylabel("Normalized flux", fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
