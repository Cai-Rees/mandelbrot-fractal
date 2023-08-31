"""
The starting points (Z_0s) are iterated using the formula in the README file. At each iteration the magnitudes are checked,
if they exceed two then they will diverge and can be considered to be outside the set.
See explanation here https://math.stackexchange.com/questions/424143/why-is-the-bailout-value-of-the-mandelbrot-set-2.
The iteration at which they exceed this limit is recorded and later used to shade the manderlbrott plot.

Set SHADED_PLOTTER to False to only produce a binary scatter plot. 
"""

import matplotlib.pyplot as plt
import numpy as np


# when true code outputs a filled contour plot otherwise plots a binary scatter plot
SHADED_PLOTTER = True

# set paramaters for sampling complex plane
NUMBER_OF_AXIS_SAMPLES = 5000
X_LOWER_BOUND = -1.8
X_UPPER_BOUND = 0.5
Y_LOWER_BOUND = -1.2
Y_UPPER_BOUND = 1.2

# number of iterations checked 
ITERATIONS = 100

# create uniform sampling and store in single array
real_parts = np.linspace(X_LOWER_BOUND, X_UPPER_BOUND, NUMBER_OF_AXIS_SAMPLES)
imaginary_parts = np.linspace(Y_LOWER_BOUND, Y_UPPER_BOUND, NUMBER_OF_AXIS_SAMPLES) * -1

complex_starting_points = np.zeros((NUMBER_OF_AXIS_SAMPLES,  NUMBER_OF_AXIS_SAMPLES), 
                                   dtype=np.complex128)

for i in range(NUMBER_OF_AXIS_SAMPLES):
    complex_starting_points[i, :] += real_parts
    complex_starting_points[:, i] += imaginary_parts * 1j
    

def mandelbrot_iterator(starting_points, number_of_iterations):
    """
    Carries out iteration rule and checks if the magnitude of Z_n exceeds 2.
    If so, removes point from starting_points array and records the iteration 
    at which this occurs in array for mandelbrott shading.
    Args:
        starting_points (numpy array (complex))
        number_of_iterations (int)
    Return:
        starting_points(numpy array (int))
    """
    
    # prepare array to store shading of contour plot
    mandelbrot_shading = np.zeros_like(starting_points, dtype=int)
    
    current_iteration_array = starting_points.copy()
    indexes_of_starting_points = np.arange(len(starting_points))
        
    
    for i in range(number_of_iterations):
        if i % 5 == 0:
            print(f"On iteration {i}")
        
        # carry out iteration rule while preserving indexing
        current_iteration_array = np.square(current_iteration_array) + starting_points
        
        # identify points still inside a magnitude limit
        still_inside_set = np.abs(current_iteration_array) <= 2
        indexes_of_points_outside_set = indexes_of_starting_points[np.invert(still_inside_set)]
        
        # record iteration at which point escapes set 
        mandelbrot_shading[indexes_of_points_outside_set] += i+1
        
        # remove these points from future iterations
        current_iteration_array = current_iteration_array[still_inside_set]
        starting_points = starting_points[still_inside_set]
        indexes_of_starting_points = indexes_of_starting_points[still_inside_set]
    
    return starting_points, mandelbrot_shading
    
points_inside_set, mandelbrot_shading = mandelbrot_iterator(complex_starting_points.flatten(), ITERATIONS)

if SHADED_PLOTTER == True:
    mycmap = plt.get_cmap('nipy_spectral')
    xv, yv = np.meshgrid(real_parts, imaginary_parts)
    Z = mandelbrot_shading.reshape(NUMBER_OF_AXIS_SAMPLES, NUMBER_OF_AXIS_SAMPLES)
    
    # Manually set the color for points with a value of 0
    Z_with_color = np.where(Z == 0, -1, Z)
    
    plt.contourf(xv, yv, Z_with_color, cmap=mycmap)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()
else:
    plt.scatter(points_inside_set.real, points_inside_set.imag, color="black", marker=".")
    plt.show()

