# Python Solutions for Computational Mathematics Homework 1

# Question 1: Roots of x^3 - 5x + 3 = 0
def f1(x):
    return x**3 - 5*x + 3

def df1(x):
    return 3*x**2 - 5

def bisection_method(f, a, b, tol=1e-3):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at a and b.")
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def newton_method(f, df, x0, tol=1e-3, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton's method did not converge.")

def secant_method(f, x0, x1, tol=1e-3, max_iter=100):
    for _ in range(max_iter):
        if abs(f(x1)) < tol:
            return x1
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
    raise ValueError("Secant method did not converge.")

# Roots for Question 1
bisection_root = bisection_method(f1, -3, 3)
newton_root = newton_method(f1, df1, 2)
secant_root = secant_method(f1, -3, 3)
print("Bisection Method Root:", bisection_root)
print("Newton's Method Root:", newton_root)
print("Secant Method Root:", secant_root)

# Question 2: Root of 2x(1 - x^2 + x)ln(x) = x^2 - 1
import numpy as np

def f2(x):
    if x <= 0:
        return np.inf  # Log is undefined for x <= 0
    return 2 * x * (1 - x**2 + x) * np.log(x) - x**2 + 1

def df2(x):
    if x <= 0:
        return np.inf  # Log is undefined for x <= 0
    return 2 * (1 - x**2 + x) * np.log(x) + 2 * x * (1 - 3 * x + 2 * x**2) / x - 2 * x

# Varying initial guesses for Newton's Method
x0_guesses = [0.1, 0.5, 0.9]
newton_steps = {}
for x0 in x0_guesses:
    try:
        root = newton_method(f2, df2, x0)
        newton_steps[x0] = root
    except ValueError as e:
        newton_steps[x0] = str(e)

print("Newton's Method Results for Question 2:", newton_steps)
