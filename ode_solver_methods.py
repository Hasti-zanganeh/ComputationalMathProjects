
import numpy as np
import matplotlib.pyplot as plt

# Function and exact solution
def f(t, x):
    return x / t + t * np.sec(x / t)

def exact_solution(t):
    return t * np.arcsin(t)

# Explicit Euler Method
def explicit_euler(f, t0, x0, t_end, h):
    t_values = [t0]
    x_values = [x0]
    while t0 < t_end:
        x0 += h * f(t0, x0)
        t0 += h
        t_values.append(t0)
        x_values.append(x0)
    return np.array(t_values), np.array(x_values)

# Implicit Euler Method
def implicit_euler(f, t0, x0, t_end, h):
    t_values = [t0]
    x_values = [x0]
    while t0 < t_end:
        t_next = t0 + h
        # Use Newton's method for implicit step
        x_next = x0  # Initial guess
        for _ in range(10):
            x_next -= (x_next - x0 - h * f(t_next, x_next)) / (1 - h * (1 / t_next))
        x_values.append(x_next)
        t0 = t_next
        t_values.append(t0)
    return np.array(t_values), np.array(x_values)

# Fourth-order Runge-Kutta Method
def runge_kutta(f, t0, x0, t_end, h):
    t_values = [t0]
    x_values = [x0]
    while t0 < t_end:
        k1 = h * f(t0, x0)
        k2 = h * f(t0 + h / 2, x0 + k1 / 2)
        k3 = h * f(t0 + h / 2, x0 + k2 / 2)
        k4 = h * f(t0 + h, x0 + k3)
        x0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t0 += h
        t_values.append(t0)
        x_values.append(x0)
    return np.array(t_values), np.array(x_values)

# Solve the ODE
t0, x0, t_end = 0.01, 0, 1
step_sizes = [2**-2, 2**-4, 2**-7]

for h in step_sizes:
    t_exp, x_exp = explicit_euler(f, t0, x0, t_end, h)
    t_imp, x_imp = implicit_euler(f, t0, x0, t_end, h)
    t_rk, x_rk = runge_kutta(f, t0, x0, t_end, h)
    t_exact = np.linspace(t0, t_end, 1000)
    x_exact = exact_solution(t_exact)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t_exact, x_exact, 'k', label='Exact Solution')
    plt.plot(t_exp, x_exp, 'o-', label=f'Explicit Euler (h={h})')
    plt.plot(t_imp, x_imp, 's-', label=f'Implicit Euler (h={h})')
    plt.plot(t_rk, x_rk, '^-', label=f'Runge-Kutta (h={h})')
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title(f'ODE Solution with Step Size h={h}')
    plt.grid()
    plt.show()
