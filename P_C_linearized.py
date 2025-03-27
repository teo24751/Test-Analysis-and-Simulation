import readData as rd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


def intersection_load(displacement,load):
    # Convert to numpy arrays for better manipulation
    displacement = np.array(displacement)*1000
    load = np.array(load)
    # Filter the data to include only displacements between 1.0 and 3.0
    mask = (displacement >= 0.6) & (displacement <= 3.0)
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


    # Predict using the model
    load_pred = model.predict(displacement_filtered_reshaped)
    # Plot the regression line for the filtered data
    plt.plot(displacement_filtered, load_pred, color='red', label="Linear fit")

    # Create the second line with a slope of slope / 1.05, starting at the same intercept
    new_slope = slope / 1.05
    new_load_pred = new_slope * displacement_filtered + intercept  # Same intercept, but adjusted slope

    # Plot the new line
    plt.plot(displacement_filtered, new_load_pred, color='green', label="Line tilted (x1.05)")

    # Add labels and legend
    plt.title("Displacement vs Load with Linear Fit and Tilted Line")
    plt.xlabel("Displacement")
    plt.ylabel("Load")
    plt.legend()

    # Show the plot
    plt.show()

    load_filtered=list(load_filtered)

    #These lines refer to the original load-displacement curve
    original_differences=list(np.abs(np.array(load_pred)-np.array(load_filtered)))
    original_intersection_error=min(original_differences)
    original_intersection_index=original_differences.index(original_intersection_error)
    original_intersection_load=load_filtered[original_intersection_index]
    original_intersection_displacement=displacement_filtered[original_intersection_index]

    new_load_pred=new_slope * displacement + intercept
    #These lines refer to the offset linearized line
    differences=list(np.abs(np.array(new_load_pred)-np.array(load)))
    intersection_error=min(differences[40:])

    intersection_index=differences.index(intersection_error)
    intersection_load=load[intersection_index]
    intersection_displacement=displacement[intersection_index]

    

    return intersection_load,intersection_displacement,original_intersection_load,original_intersection_displacement




    

    
