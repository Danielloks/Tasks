import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    x_values = [4, 5, 6]
    y_values = [function(x) for x in x_values]

    for x, y in zip(x_values, y_values):
        print(f"f({x}) = {y}")

    a = 4.5
    f_a = function(a)
    L_a = lagrange_polynomial(a, x_values, y_values)
    error = abs(f_a - L_a)

    print(f"f({a}) = {f_a}")
    print(f"L({a}) = {L_a}")
    print(f"Error = {error}")

    # Построение графика функции и интерполяционного полинома Лагранжа
    x_range = np.linspace(3.5, 6.5, 400)
    y_function = [function(x) for x in x_range]
    y_interpolated = [lagrange_polynomial(x, x_values, y_values) for x in x_range]

    plt.plot(x_range, y_function, label="Function")
    plt.plot(x_range, y_interpolated, label="Interpolated", linestyle='--')
    plt.scatter(x_values, y_values, color='red', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function vs Interpolated Polynomial')
    plt.legend()
    plt.grid(True)
    plt.show()

def function(x):
    return math.pow(math.log(x), 12.0 / 5.0)

def lagrange_polynomial(x, x_values, y_values):
    result = 0.0
    n = len(x_values)

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

main()
