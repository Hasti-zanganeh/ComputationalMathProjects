
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d

# Function to interpolate
def f(x):
    return 1 / (1 + x**2)

# Degree 40 polynomial interpolation
def polynomial_interpolation(x, y, x_eval):
    coeffs = np.polyfit(x, y, deg=len(x)-1)
    return np.polyval(coeffs, x_eval)

# Equally spaced nodes
def equally_spaced_nodes(a, b, n):
    return np.linspace(a, b, n)

# Spline and Polynomial Analysis
def spline_and_polynomial_analysis():
    x_nodes = equally_spaced_nodes(-5, 5, 41)
    y_nodes = f(x_nodes)
    x_eval = np.linspace(0, 5, 101)

    # Spline interpolations
    linear_spline = interp1d(x_nodes, y_nodes, kind='linear')(x_eval)
    quadratic_spline = interp1d(x_nodes, y_nodes, kind='quadratic')(x_eval)
    cubic_spline = CubicSpline(x_nodes, y_nodes, bc_type='natural')(x_eval)

    # Degree 40 polynomial interpolation
    polynomial = polynomial_interpolation(x_nodes, y_nodes, x_eval)

    # Original function
    y_eval = f(x_eval)

    # Plot
    plt.figure(figsize=(12, 8))
    plt.plot(x_eval, y_eval, 'k', label='f(x) = 1/(1 + x^2)')
    plt.plot(x_eval, linear_spline, '--', label='Linear Spline')
    plt.plot(x_eval, quadratic_spline, '--', label='Quadratic Spline')
    plt.plot(x_eval, cubic_spline, '--', label='Natural Cubic Spline')
    plt.plot(x_eval, polynomial, '--', label='Degree 40 Polynomial')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Spline and Polynomial Analysis')
    plt.grid()
    plt.show()

spline_and_polynomial_analysis()
