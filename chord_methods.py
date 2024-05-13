import math

def find_initial_guesses(f, x_range=(0.01, 10), step=0.1):
    initial_guesses = []
    x_min, x_max = x_range
    x = x_min
    while x <= x_max:
        if f(x) * f(x + step) < 0:
            initial_guesses.append((x, x + step))
        x += step
    return initial_guesses

def chord_method(f, x0, x1, tol=1e-6, max_iter=100):
    print("Метод хорд")
    print(f"Начальное приближение: x0 = {x0}, x1 = {x1}")
    for i in range(max_iter):
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Итерация {i+1}: x{i+2} = {x_next:.6f}")
        if abs(x_next - x1) < tol:
            print(f"Примерное решение: x ≈ {x_next:.6f}")
            return x_next
        x0, x1 = x1, x_next
    print("Не удалось найти решение")
    return None

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    print("Метод секущих")
    print(f"Начальное приближение: x0 = {x0}, x1 = {x1}")
    for i in range(max_iter):
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Итерация {i+1}: x{i+2} = {x_next:.6f}")
        if abs(x_next - x1) < tol:
            print(f"Примерное решение: x ≈ {x_next:.6f}")
            return x_next
        x0, x1 = x1, x_next
    print("Не удалось найти решение")
    return None

# Уравнения
equations = [
    ("ln(x) + x*x - 3", lambda x: math.log(x) + x*x - 3),
    ("ln(x)*ln(x) + 0.25*x - 3", lambda x: math.log(x) * math.log(x) + 0.25 * x - 3),
    ("2 * ln(x) + 0.01 * x*x", lambda x: 2 * math.log(x) + 0.01 * x*x),
    ("2 * ln(x) + x - 7", lambda x: 2 * math.log(x) + x - 7),
    ("2 * ln(x)*ln(x) + 2 * x*x - 3", lambda x: 2 * math.log(x) * math.log(x) + 2 * x*x - 3)
]

for i, (equation_str, f) in enumerate(equations, start=1):
    print(f"\nУравнение {i}: {equation_str}")
    guesses = find_initial_guesses(f)
    if guesses:
        for j, (x0, x1) in enumerate(guesses, start=1):
            print(f"\nНачальные приближения для корня {j}: x0 = {x0}, x1 = {x1}")
            chord_method(f, x0, x1)
            secant_method(f, x0, x1)
    else:
        print("Не удалось найти начальные приближения")
