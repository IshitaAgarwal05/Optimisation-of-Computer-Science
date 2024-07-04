# Steepest Descent Indirect Search Method - type 1
# Author: Ishita Agarwal

  # Slow convergence
  # Less efficient for non-quadratic equations - since,the solution may get stuck at a local optima.


from tabulate import tabulate
import numpy as np
import sympy as sp
import math

def func(x): return x[0]**2 - x[0]*x[1] + x[1]**2               # Objective Function
def grad(x):
  x1, x2 = sp.symbols('x1 x2')
  f_symbolic = func([x1, x2])
  partial_x1 = sp.diff(f_symbolic, x1)
  partial_x2 = sp.diff(f_symbolic, x2)
  partial_x1_value = partial_x1.subs([(x1, x[0]), (x2, x[1])])
  partial_x2_value = partial_x2.subs([(x1, x[0]), (x2, x[1])])
  grad = np.array([partial_x1_value , partial_x2_value])
  return grad

def steepest_descent(x,epsilon,l):
  table = []
  k = 0
  d = -grad(x)
  mag = math.sqrt(d[0]**2+d[1]**2)
  table.append([k, x[0],x[1],mag,func(x)])
  print(grad(x))
  print(d)
  mag = math.sqrt(d[0]**2+d[1]**2)
  while(mag > epsilon):
    k+=1
    d = -grad(x)
    x = x + l*d
    mag = math.sqrt(d[0]**2+d[1]**2)
    table.append([k,x[0],x[1],mag,func(x)])
  return table,x,func(x)

x1 = 1
x2 = 2
x = np.array([x1,x2])

epsilon = 0.05
l = 0.5
table, x, ans = steepest_descent(x,epsilon,l)

print(tabulate(table, headers=["k", "x1", "x2","d","f(x)"], tablefmt="grid"))
print("Value of x:", x)
print("Minimum f(x):", ans)