# Identify Convexity of 2*2 Hessian matrix for given 2-degree objective function in three variables
# Author: Ishita Agarwal

import sympy as sp
x, y, z = sp.symbols('x y z')
f = x**2 + 2*x*y + 3*(y**2)+4*(z**2)-5*y*z              # Objective function

gradient = [sp.diff(f, var) for var in (x, y, z)]
gradient_matrix = sp.Matrix(gradient)
critical_points = sp.solve(gradient, (x, y, z))
print("Gradient matrix: \n", gradient_matrix)

if len(critical_points) > 0:
    print("Critical Points:", critical_points)
else:
    print("No critical points found.")

hessian_matrix = sp.hessian(f, (x, y, z))
print("Hessian Matrix: \n", hessian_matrix)

det1 = hessian_matrix[0, 0]
det2 = hessian_matrix.det()

if det1_value > 0 and det2_value > 0:
    print("The Hessian matrix is positive definite. \nThis implies that the function is CONVEX. \nWe'll get the minima at the critical point.")
elif det1_value == 0 and det2_value == 0:
    print("The test is inconclusive.")
elif det1_value > 0 and det2_value < 0:
    print("The Hessian matrix is negative semidefinite. \nThis implies that the function is CONCAVE. \nWe'll get the maxima at the critical point.")
else:
    print("The definiteness of the Hessian matrix cannot be determined. There lies a saddle point at the critical point.")