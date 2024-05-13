import numpy as np

def solve_system(equations, initial_guess=(0.0, 0.0), tolerance=0.0001, max_iterations=10000):
    x, y = initial_guess
    num_equations = len(equations)

    iteration = 0
    has_converged = False

    while iteration < max_iterations and not has_converged:
        old_x, old_y = x, y
        errors = []

        for i in range(num_equations):
            eq = equations[i]

            if i == 0:
                y = eq(x, y)
            else:
                x = eq(x, y)

            errors.append(abs(x - old_x))
            errors.append(abs(y - old_y))

        if all(error < tolerance for error in errors):
            has_converged = True

        iteration += 1

    if has_converged:
        print(f"Converged in {iteration} iterations.")
        print(f"Solution: x = {x}, y = {y}")
    else:
        print("The method did not converge.")

# Define equations as lambda functions
equations1 = [
    lambda x, y: 1.5 - np.cos(x),
    lambda x, y: np.arcsin(np.sin(2*x - 1)) + 0.5
]

solve_system(equations1)
