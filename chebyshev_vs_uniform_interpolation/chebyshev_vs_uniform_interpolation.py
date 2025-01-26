
import numpy as np
import matplotlib.pyplot as plt

# Function to interpolate
def f(x):
    return 1 / (x**2 + 1)

# Equally spaced nodes
def equally_spaced_nodes(a, b, n):
    return np.linspace(a, b, n)

# Chebyshev nodes
def chebyshev_nodes(a, b, n):
    return 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))

# Interpolating polynomial using Lagrange form
def lagrange_interpolation(x, y, x_eval):
    n = len(x)
    p = np.zeros_like(x_eval)
    for i in range(n):
        li = np.ones_like(x_eval)
        for j in range(n):
            if i != j:
                li *= (x_eval - x[j]) / (x[i] - x[j])
        p += y[i] * li
    return p

# Plotting
def plot_interpolation(a, b, n_values):
    x_plot = np.linspace(a, b, 1000)
    f_plot = f(x_plot)
    
    plt.figure(figsize=(12, 8))
    for n in n_values:
        # Equally spaced nodes
        x_eq = equally_spaced_nodes(a, b, n)
        y_eq = f(x_eq)
        p_eq = lagrange_interpolation(x_eq, y_eq, x_plot)

        # Chebyshev nodes
        x_ch = chebyshev_nodes(a, b, n)
        y_ch = f(x_ch)
        p_ch = lagrange_interpolation(x_ch, y_ch, x_plot)

        # Plotting
        plt.plot(x_plot, p_eq, '--', label=f'Equally Spaced, n={{n}}')
        plt.plot(x_plot, p_ch, '-', label=f'Chebyshev, n={{n}}')

    plt.plot(x_plot, f_plot, 'k', label='f(x) = 1/(x^2 + 1)')
    plt.legend()
    plt.title('Interpolating Polynomial Comparison: Equally Spaced vs Chebyshev Nodes')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Values of n
n_values = [5, 11, 21, 41]
plot_interpolation(-5, 5, n_values)
