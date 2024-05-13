import numpy as np

def integrate_gauss(f, a, b, n=10):
    x, w = np.polynomial.legendre.leggauss(n)
    return np.sum(w * f((b - a) / 2 * x + (b + a) / 2))

def func(x):
    return np.cos(x - 12 * x**3)

lower_limit = 0.0
upper_limit = np.pi

integral_value = integrate_gauss(func, lower_limit, upper_limit)

print(f"The value of the definite integral from {lower_limit} to {upper_limit} using Gauss quadrature is: {integral_value}")
