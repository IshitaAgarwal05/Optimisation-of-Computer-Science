# Identify Convexity of n*n Hessian matrix for given n-degree objective function in two variables
# Author: Ishita Agarwal

import sympy as sp

x, y = sp.symbols('x y')
f =  -x**4 - 3*(x**2) + 5*x - 2*x*y - y**2              # Objective Function

gradient = [sp.diff(f, var) for var in (x, y)]
gradient_matrix = sp.Matrix(gradient)
critical_points = sp.solve(gradient, (x, y))
print("Gradient matrix: \n", gradient_matrix)

if len(critical_points) > 0:
    print("Critical Points:", critical_points)
else:
    print("No critical points found.")

hessian_matrix = sp.hessian(f, (x, y))
print("Hessian Matrix: \n", hessian_matrix)

det1 = hessian_matrix[0, 0]
det2 = hessian_matrix.det()

# Checking if the Hessian is positive definite or not
det1_value = det1.subs({x: critical_points[0][0], y: critical_points[0][1]})
det2_value = det2.subs({x: critical_points[0][0], y: critical_points[0][1]})

if det1_value > 0 and det2_value > 0:
    print("The Hessian matrix is positive definite. \nThis implies that the function is CONVEX. \nWe'll get the minima at the critical point.")
elif det1_value == 0 and det2_value == 0:
    print("The test is inconclusive.")
elif det1_value > 0 and det2_value < 0:
    print("The Hessian matrix is negative semidefinite. \nThis implies that the function is CONCAVE. \nWe'll get the maxima at the critical point.")
else:
    print("The definiteness of the Hessian matrix cannot be determined. There lies a saddle point at the critical point.")