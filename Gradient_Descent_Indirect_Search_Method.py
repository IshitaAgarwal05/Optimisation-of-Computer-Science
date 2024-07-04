# Gradient Descent Indirect Search Method - type 2
# Author: Ishita Agarwal

  # update weight and bias

import numpy as np
import math

def total_cost(x):
    return 15000*(math.sqrt(1+x**2))  + (9000*(4-x))            # Objective function

def gradient(x):
    return 15000*x/(math.sqrt(1+x**2)) - 9000

def gradient_descent(learning_rate=0.1, max_iterations=1000, tolerance=1e-6):
    # Initial guess for x (midpoint between 0 and 4 km)
    x = 2
    iteration = 0

    while iteration < max_iterations:
        grad = gradient(x)
        x_new = x - learning_rate * grad
        if abs(x_new - x) < tolerance: break
        x = x_new
        iteration += 1
    return x, total_cost(x)

optimal_x_gradient, min_cost_gradient = gradient_descent()

print("Gradient Search Method (Gradient Descent):")
print("Optimal Distance from P to T:", optimal_x_gradient, "kilometers")
print("Minimum Cost:", min_cost_gradient, "Rupees")