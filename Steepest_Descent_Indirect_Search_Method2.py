# Steepest Descent Indirect Search Method - type 2
# Author: Ishita Agarwal

  # Slow convergence
  # Less efficient for non-quadratic equations - since,the solution may get stuck at a local optima.

import numpy as np
def objective_function(x):
    return 15000 * np.sqrt(1 + x**2) + 9000 * (4 - x)

def gradient(x):
    return (15000 * x) / np.sqrt(1 + x**2) - 9000

def hessian(x):
    return 15000 / ((1 + x**2)**(3/2))

def line_search(x, grad):
    alpha = 0.1
    beta = 0.5
    t = 1.0
    while objective_function(x - t * grad) >= objective_function(x) - alpha * t * np.dot(grad, grad):
        t *= beta
    return t

def steepest_descent(max_iterations, tolerance):
    x = 0  # Initial guess
    for i in range(max_iterations):
        grad = gradient(x)
        Si = -grad
        lam = line_search(x, grad)
        x += lam * Si

        print(f"Iteration {i + 1}:")
        print(f"  x = {x:.8f}")
        print(f"  f(x) = {objective_function(x):.8f}")
        print(f"  Gradient = {grad:.8f}")
        print(f"  Direction vector Si = {Si:.8f}")
        print(f"  Step size lambda = {lam:.8f}")

        if np.linalg.norm(grad) < tolerance: break

    print("\nConvergence reached.")
    print(f"Total number of iterations: {i + 1}")
    print(f"Optimal solution: x = {x:.8f}")
    print(f"Minimum value: f(x) = {objective_function(x):.8f}")

max_iterations = 1000
tolerance = 1e-6
steepest_descent(max_iterations, tolerance)