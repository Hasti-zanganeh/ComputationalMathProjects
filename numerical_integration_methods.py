
import numpy as np

# Function to integrate
def f(x):
    return np.cos(2 * x) * np.exp(-x)

# Composite Trapezoidal Rule
def composite_trapezoidal(a, b, tol):
    n = 1
    integral = (b - a) * (f(a) + f(b)) / 2
    while True:
        n *= 2
        h = (b - a) / n
        x_mid = np.arange(a + h, b, h)
        integral_new = h * (f(a) + 2 * sum(f(x_mid)) + f(b)) / 2
        if abs(integral_new - integral) < tol:
            return integral_new, n
        integral = integral_new

# Composite Simpson's Rule
def composite_simpson(a, b, tol):
    n = 2  # Must be even
    h = (b - a) / n
    integral = h / 3 * (f(a) + 4 * f(a + h) + f(b))
    while True:
        n *= 2
        h = (b - a) / n
        x_odd = np.arange(a + h, b, 2 * h)
        x_even = np.arange(a + 2 * h, b, 2 * h)
        integral_new = h / 3 * (f(a) + 4 * sum(f(x_odd)) + 2 * sum(f(x_even)) + f(b))
        if abs(integral_new - integral) < tol:
            return integral_new, n
        integral = integral_new

# Composite Midpoint Rule
def composite_midpoint(a, b, tol):
    n = 1
    h = (b - a) / n
    x_mid = np.linspace(a + h / 2, b - h / 2, n)
    integral = h * sum(f(x_mid))
    while True:
        n *= 2
        h = (b - a) / n
        x_mid = np.linspace(a + h / 2, b - h / 2, n)
        integral_new = h * sum(f(x_mid))
        if abs(integral_new - integral) < tol:
            return integral_new, n
        integral = integral_new

# Integration bounds and tolerance
a, b = 0, 2 * np.pi
tol = 1.0e-5

# Results
trap_result, trap_steps = composite_trapezoidal(a, b, tol)
simp_result, simp_steps = composite_simpson(a, b, tol)
mid_result, mid_steps = composite_midpoint(a, b, tol)

print("Composite Trapezoidal Rule:")
print(f"Result = {trap_result}, Steps = {trap_steps}")

print("Composite Simpson's Rule:")
print(f"Result = {simp_result}, Steps = {simp_steps}")

print("Composite Midpoint Rule:")
print(f"Result = {mid_result}, Steps = {mid_steps}")
