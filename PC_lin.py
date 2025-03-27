import readData as rd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
data1 = rd.load_displacement_curve(3)
#print(data1)

# Prepare the displacement and load lists
displacement, load = [], []
for i in range(len(data1)):
    load.append(data1[i][0])  # Assuming the first element is load
    displacement.append(data1[i][1])  # Assuming the second element is displacement

# Convert to numpy arrays for better manipulation
displacement = np.array(displacement)
load = np.array(load)

# Filter the data to include only displacements between 0.6 and 4.0
mask = (displacement >= 0.6) & (displacement <= 4.0)
displacement_filtered = displacement[mask]
load_filtered = load[mask]

# Scatter plot of the entire data
plt.scatter(displacement, load, label="Full Data", color='blue', s = 2)

# Create and fit the model with the filtered data
model = LinearRegression()
displacement_filtered_reshaped = displacement_filtered.reshape(-1, 1)  # Reshape for sklearn
model.fit(displacement_filtered_reshaped, load_filtered)

# Get the model parameters
slope = model.coef_[0]
intercept = model.intercept_

# Print the results
#print(f"Slope: {slope}")
#print(f"Intercept: {intercept}")

# Predict using the model
load_pred = model.predict(displacement_filtered_reshaped)

# Plot the regression line for the filtered data
plt.plot(displacement_filtered, load_pred, color='red', label="Linear fit (0.6 <= displacement <= 4.0)")

# Create the second line with a slope of slope * 1.05, starting at the same intercept
new_slope = slope / 1.05
new_load_pred = new_slope * displacement_filtered + intercept  # Same intercept, but adjusted slope

# Plot the new line
plt.plot(displacement_filtered, new_load_pred, color='green', label="Line tilted 1.05 times")

# Add labels and legend
plt.title("Displacement vs Load with Linear Fit and Tilted Line")
plt.xlabel("Displacement")
plt.ylabel("Load")
plt.legend()

# Show the plot
plt.show()
