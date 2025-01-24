import numpy as np
def f(x):
    return x * np.exp(x)
def f_prime(x):
    return (1 + x) * np.exp(x)  # f'(x)
def f_double_prime(x):
    return (2 + x) * np.exp(x)  # f''(x)
def euler_method(f_prime, f_double_prime, x0, x_end, h):
    x_values = np.arange(x0, x_end + h, h)
    f_prime_approx = []
    f_double_prime_approx = []
   
    f_prime_val = f_prime(x0)
    f_double_prime_val = f_double_prime(x0)
    for x in x_values:
        f_prime_approx.append(f_prime_val)
        f_double_prime_approx.append(f_double_prime_val)
        f_prime_val += h * f_double_prime_val
        f_double_prime_val += h * ((3 + x) * np.exp(x))
    return x_values, f_prime_approx, f_double_prime_approx

# Defining parameters
x0 = 1.5
x_end = 2.5
h = 0.1
x_values, f_prime_approx, f_double_prime_approx = euler_method(f_prime, f_double_prime, x0, x_end, h)

print("x-values\tf'(x) Approximation\tf''(x) Approximation")
for x, fp, fpp in zip(x_values, f_prime_approx, f_double_prime_approx):
    print(f"{x:.1f}\t\t{fp:.4f}\t\t\t{fpp:.4f}")
