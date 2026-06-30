import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# loading the local csv file
project_root = Path(__file__).resolve().parents[2]
train_path = project_root / "data" / "raw" / "exoTrain.csv"
test_path = project_root / "data" / "raw" / "exoTest.csv"

train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)

# Check the dimensions of the matrix

print(f"Train data shape: {train_data.shape}")
print(f"Test data shape: {test_data.shape}")

# Extract features and labels (the first column)
y_train_raw = train_data.iloc[:, 0].values
y_test_raw = test_data.iloc[:, 0].values

# Convert Kaggle Labels(2-1 for planets, 1-0 for no planets)
y_train=np.where(y_train_raw==2,1,0)
y_test=np.where(y_test_raw==2,1,0)

#Extract just the raw light curve data(drop the label column)
X_train = train_data.iloc[:, 1:].values
X_test= test_data.iloc[:, 1:].values

#Quick sanity check: How many planets do we actually have?
print(f"Number of confirmed planet stars in training set: {np.sum(y_train)}")
print(f"Number of normal stars in training set: {len(y_train) - np.sum(y_train)}")

# Find the index of the first planet star (where y_train == 1)
planet_indices = np.where(y_train == 1)[0]
first_planet_idx = planet_indices[0]

#plot the first planet star
plt.figure(figsize=(14, 4))
plt.plot(X_train[first_planet_idx], color='darkblue', lw=0.5)
plt.title(f"Exoplanet light curve - Star index {first_planet_idx}", fontsize=14)
plt.xlabel("Time(sequential observations)", fontsize=12)
plt.ylabel("Normalized flux", fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

