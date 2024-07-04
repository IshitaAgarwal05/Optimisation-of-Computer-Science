# Direct Search Methods for optimisation
# Author: Ishita Agarwal

# Golden Section Direct Search Method 
    # r = (0.618)*(b-a)
    # x1 = a + r
    # x2 = b - r
    # gets the minima/maxima of a unimodal function
    
# Fibonacci-Virhanka Direct Search Method
    # r = [F(n-2)/Fn](b-a)
    # x1 = a + r
    # x2 = b - r

import math

def golden_ratio_search(func, a, b, tol=1e-6):
    phi = (1 + math.sqrt(5)) / 2
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    while abs(c - d) > tol:
        if func(c) < func(d):
            b = d
        else:
            a = c
        c = b - (b - a) / phi
        d = a + (b - a) / phi
    return (b + a) / 2

def fibonacci_search(func, a, b, n=10):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    for i in range(n):
        x1 = a + (fibonacci(n-i-1) / fibonacci(n-i+1)) * (b - a)
        x2 = a + (fibonacci(n-i) / fibonacci(n-i+1)) * (b - a)
        if func(x1) < func(x2):
            b = x2
        else:
            a = x1
    return (a + b) / 2

def quadratic_function(x):
    return (x - 3) ** 2 + 5

# Using Golden Ratio search
min_x_golden = golden_ratio_search(quadratic_function, 0, 5)
print("Minimum using Golden Ratio search:", min_x_golden)

# Using Fibonacci search
min_x_fibonacci = fibonacci_search(quadratic_function, 0, 5)
print("Minimum using Fibonacci search:", min_x_fibonacci)