# Newton's Indirect Search Method - type 1
# Author: Ishita Agarwal

  # Converges rapidly, but diverges if, Hf != positive definite
  # Complex because of inverse([Hf])
  # Derived through Taylor series

from tabulate import tabulate
import numpy as np
import sympy as sp

def func(x):
  return x[0]**2 - x[0]*x[1] + 3*x[1]**2            # Objective function

def gradient(x):
  x1, x2 = sp.symbols('x1 x2')
  f_symbolic = func([x1, x2])
  partial_x1 = sp.diff(f_symbolic, x1)
  partial_x2 = sp.diff(f_symbolic, x2)
  partial_x1_value = partial_x1.subs([(x1, x[0]), (x2, x[1])])
  partial_x2_value = partial_x2.subs([(x1, x[0]), (x2, x[1])])
  grad = np.array([partial_x1_value , partial_x2_value])
  return grad

def hessian(x):
  x1, x2 = sp.symbols('x1 x2')
  f_symbolic = func([x1, x2])
  partial_x1_x1 = sp.diff(f_symbolic, x1, x1)
  partial_x2_x2 = sp.diff(f_symbolic, x2, x2)
  partial_x1_x2 = sp.diff(f_symbolic, x1, x2)
  partial_x2_x1 = sp.diff(f_symbolic, x2, x1)
  partial_x1_x1_value = partial_x1_x1.subs([(x1,x[0]), (x2,x[1])])
  partial_x2_x2_value = partial_x2_x2.subs([(x1,x[0]), (x2,x[1])])
  partial_x1_x2_value = partial_x1_x2.subs([(x1,x[0]), (x2,x[1])])
  partial_x2_x1_value = partial_x2_x1.subs([(x1,x[0]), (x2,x[1])])
  hessian_matrix = np.array([[partial_x1_x1, partial_x1_x2],[partial_x2_x1, partial_x2_x2]],dtype=float)
  return hessian_matrix

def newtons_method(x):
  table = []
  k = 0
  table.append([k, x1, x2, func(x), gradient(x)])
  while(((func(x)>0) or (x1 == x2)) and k<50):
    k += 1
    hess_inv = np.linalg.inv(hessian(x))
    grad = gradient(x)
    x = x - hess_inv.dot(grad)
    table.append([k, x[0], x[1], func(x), gradient(x)])
  return table, x, func(x)

x1 = 1
x2 = 2
x = np.array([x1,x2])
table, x, ans = newtons_method(x)

print(tabulate(table, headers=["k", "x1", "x2", "f(x)", "Gradient"],
tablefmt="grid"))
print("Value of x:", x)
print("Minimum f(x):", ans)