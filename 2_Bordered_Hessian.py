# Identify Convexity of 2*2 Bordered Hessian matrix for given 2-degree objective function in two variables
# Author: Ishita Agarwal

import sympy as sp
x, y, lam = sp.symbols('x y lambda')

f = -x**2 + x*y - y**2      # Objective function
g = x + y - 1               # Constraints

L = f + lam * g
grad_L = [sp.diff(L, var) for var in (x, y, lam)]
critical_points = sp.solve(grad_L, (x, y, lam))
H = sp.hessian(L, (x, y))

bordered_Hessian = sp.Matrix([[0, sp.diff(g, x), sp.diff(g, y)],
                              [sp.diff(g, x), H[0, 0], H[0, 1]],
                              [sp.diff(g, y), H[1, 0], H[1, 1]]])

extrema = []
for point in critical_points:
    if isinstance(point, dict):
        numeric_point = {var: val.evalf() for var, val in point.items()}
        extrema.append((numeric_point, f.subs(numeric_point)))

if bordered_Hessian.is_positive_definite:
    if f.subs({x: critical_points[0][0], y: critical_points[0][1]}) < 0:
        print("The function is convex and has a minimum at:", extrema[0][0])
    else:
        print("The function is concave and has a maximum at:", extrema[0][0])
elif bordered_Hessian.is_negative_definite:
    print("The function is concave.")
elif bordered_Hessian.is_indefinite:
    print("The test is inconclusive.")