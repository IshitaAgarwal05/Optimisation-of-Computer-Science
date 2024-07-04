# Identify Convexity of 2*2 Hessian matrix for given 2-degree objective function in two variables
# Author: Ishita Agarwal

import sympy as sp
x, y = sp.symbols('x y')
f = x*y     # Objectve function

gradient = [sp.diff(f, var) for var in (x, y)]
gradient_matrix = sp.Matrix(gradient)
critical_points = sp.solve(gradient, (x, y))
print("Gradient matrix: \n", gradient_matrix)

# Check for critical points of the objective function
if len(critical_points) > 0: print("Critical Points:", critical_points)
else: print("No critical points found.")

hessian_matrix = sp.hessian(f, (x, y))
print("Hessian Matrix: \n", hessian_matrix)

det1 = hessian_matrix[0,0]
det2 = hessian_matrix.det()

#Checking if the Hessian is positive definite or not
if (det1>0) and (det2>0):         #positive
  print("The Hessian matrix is positive definite. \nThis implies, that the function is CONVEX. \nThat is, we'll get the minima at the critical point.")

elif (det1==0) and (det2==0):     #zero
  print("The test is inconclusive.")

elif (det1>0) and (det2<0):       #semi-negative
  print("The Hessian matrix is negative semidefinite. \nThis implies, that the function is CONCAVE. \nThat is, we'll get the maxima at the critical point.")

else:                             #none
  print("The definiteness of the Hessian matrix cannot be determined. There lies a saddle point at the critical point.")