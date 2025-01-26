
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d

# Function to interpolate
def f(x):
    return 1 / (x**2 + 1)

# Equally spaced nodes
def equally_spaced_nodes(a, b, n):
    return np.linspace(a, b, n)

# Plotting splines
def plot_splines(a, b, n_values):
    x_plot = np.linspace(a, b, 1000)
    f_plot = f(x_plot)
    
    plt.figure(figsize=(12, 8))
    for n in n_values:
        # Equally spaced nodes
        x_nodes = equally_spaced_nodes(a, b, n)
        y_nodes = f(x_nodes)

        # Linear spline
        linear_spline = interp1d(x_nodes, y_nodes, kind='linear')
        p_linear = linear_spline(x_plot)

        # Natural cubic spline
        cubic_spline = CubicSpline(x_nodes, y_nodes, bc_type='natural')
        p_cubic = cubic_spline(x_plot)

        # Plotting
        plt.plot(x_plot, p_linear, '--', label=f'Linear Spline, n={{n}}')
        plt.plot(x_plot, p_cubic, '-', label=f'Natural Cubic Spline, n={{n}}')

    plt.plot(x_plot, f_plot, 'k', label='f(x) = 1/(x^2 + 1)')
    plt.legend()
    plt.title('Linear Spline vs Natural Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Values of n
n_values = [5, 11, 21]
plot_splines(-5, 5, n_values)
