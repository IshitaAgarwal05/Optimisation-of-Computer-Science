# Golden Section Direct Search Methods for optimisation
# Author: Ishita Agarwal

    # r = (0.618)*(b-a)
    # x1 = a + r
    # x2 = b - r
    # gets the minima/maxima of a unimodal function

from tabulate import tabulate
import math

def func(x: float):
  return 15000*(math.sqrt(1+x**2)) + (9000 * (4-x))

def golden_section_search(a, b, err):
  golden_ratio = (math.sqrt(5) - 1) / 2
  d = golden_ratio*(b-a)
  x1 = a + d
  x2 = b - d
  f_x1 = func(x1)
  f_x2 = func(x2)
  table = []
  k = 0
  S = "-"
  table.append([k, a, b, d, x1, x2, f_x1, f_x2,S])
  while (abs(a - b) > err):
    k += 1
    if f_x1 < f_x2:
      a = x2
      d = golden_ratio*(b-a)
      x1 = a + d
      x2 = b - d
      f_x1 = func(x1)
      f_x2 = func(x2)
      S = 'R'
    else:
      b = x1
      d = golden_ratio*(b-a)
      x1 = a + d
      x2 = b - d
      f_x1 = func(x1)
      f_x2 = func(x2)
      S = 'L'
    table.append([k, a, b, d, x1, x2, f_x1, f_x2, S])
  x = (a + b) / 2
  ans = round(func(x), 3)
  return table, x, ans

a = 0
b = 1
Error = 0.001
table, x, ans = golden_section_search(a, b , Error)
print(tabulate(table, headers=["k", "a", "b", "d", "x1", "x2", "f(x1)", "f(x2)", "a/b"], tablefmt="grid"))
print("Value of x:", x)
print("Min f(x):",ans)