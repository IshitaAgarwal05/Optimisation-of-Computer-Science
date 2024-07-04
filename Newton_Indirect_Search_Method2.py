# Newton's Indirect Search Method - type 2
# Author: Ishita Agarwal

  # Converges rapidly, but diverges if, Hf != positive definite
  # Complex because of inverse([Hf])
  # Derived through Taylor series

import numpy as np
import math
from tabulate import tabulate

def function(x, y):
    return 15000*(math.sqrt(1+x**2)) + (9000 * (4-x))           # Objective Function

def gradient(x, y):
    df_dx = 2*x + 6*x - y
    df_dy = -x
    return np.array([df_dx, df_dy])

def hessian(x, y):
    df2_dx2 = 2 + 6
    df2_dy2 = 0
    df2_dxdy = -1
    return np.array([[df2_dx2, df2_dxdy], [df2_dxdy, df2_dy2]])

def newton_indirect_search(x, y, tol=1e-6, max_iter=100):
    iter_count = 0
    gradient_norm = np.linalg.norm(gradient(x, y))
    table = []
    headers = ["Iteration", "(x, y)", "f(x, y)", "Gradient", "Direction", "Step Size"]

    while gradient_norm > tol and iter_count < max_iter:
        grad = gradient(x, y)
        hess = hessian(x, y)
        s = -grad
        lambda_i = np.linalg.inv(hess).dot(s)
        x_new = x + lambda_i[0] * s[0]
        y_new = y + lambda_i[1] * s[1]
        gradient_norm = np.linalg.norm(gradient(x_new, y_new))

        table.append([iter_count + 1, f"({x:.6f}, {y:.6f})", function(x, y), grad, s, lambda_i])
        x, y = x_new, y_new
        iter_count += 1
    print(tabulate(table, headers=headers, tablefmt="grid"))
    return x, y, function(x, y)

x_0 = 1
y_0 = 2
min_x, min_y, min_value = newton_indirect_search(x_0, y_0)
print("\nMinimum value found at (x, y) =", (min_x, min_y))
print("Minimum function value f(x, y) =", min_value)