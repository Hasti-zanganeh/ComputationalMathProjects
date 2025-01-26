
import numpy as np

# Functions for the system
def f1(x1, x2):
    return x1**2 + x2**2 - 2

def f2(x1, x2):
    return x1 - x2

# Jacobian matrix
def jacobian(x1, x2):
    return np.array([[2*x1, 2*x2], [1, -1]])

# Newton's method for nonlinear systems
def newton_nonlinear_system(x0, tol=1e-5, max_iter=100):
    x = np.array(x0, dtype=float)
    solutions = []
    for _ in range(max_iter):
        F = np.array([f1(x[0], x[1]), f2(x[0], x[1])])
        J = jacobian(x[0], x[1])
        dx = np.linalg.solve(J, -F)
        x += dx
        solutions.append(x.copy())
        if np.linalg.norm(dx) < tol:
            return x, solutions
    raise ValueError("Newton's method did not converge")

# Solve the system with two initial guesses
sol1, path1 = newton_nonlinear_system([1, 1])
sol2, path2 = newton_nonlinear_system([-1, -1])

print("Solution 1:", sol1)
print("Solution 2:", sol2)
