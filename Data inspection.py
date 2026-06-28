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

# Extract features and labels from the training set
X_train = train_data.drop(columns="LABEL").values
y_train = train_data["LABEL"].values

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