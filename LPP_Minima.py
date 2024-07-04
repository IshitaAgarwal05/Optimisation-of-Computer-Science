# Linear Programming Problems - Minimisation
# Author: Ishita Agarwal

from scipy.optimize import minimize

def objective_function(x):
    P1, P2 = x
    return -1 * (10**5 * (22*P1 - P1*2 + 18*P2 - P2*2) - 105*0.06*(4 - P1 + P2) - 0.08)

initial_guess = [10, 10]
bounds = [(0, 22), (0, 18)]  # Prices cannot be negative and cannot exceed 22 and 18 respectively
result = minimize(objective_function, initial_guess, bounds=bounds)
optimal_prices = result.x
optimal_profit = -1 * result.fun

print("Optimal Prices (P1, P2):", optimal_prices)
print("Optimal Profit:", optimal_profit)