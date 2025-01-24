import numpy as np

def f(x):
    return x * np.exp(x)

def f_prime(x):
    return (1 + x) * np.exp(x)

def f_double_prime(x):
    return (2 + x) * np.exp(x)

def runge_kutta4(f_prime, f_double_prime, x0, x_end, h):
    x_values = np.arange(x0, x_end + h, h)
    f_prime_approx = []
    f_double_prime_approx = []
    
    f_prime_val = f_prime(x0)
    f_double_prime_val = f_double_prime(x0)
    
    for x in x_values:
        f_prime_approx.append(f_prime_val)
        f_double_prime_approx.append(f_double_prime_val)
        
        k1 = h * f_double_prime(x)
        k2 = h * f_double_prime(x + h/2)
        k3 = h * f_double_prime(x + h/2)
        k4 = h * f_double_prime(x + h)
        f_prime_val += (k1 + 2*k2 + 2*k3 + k4)/6
        
        k1 = h * (3 + x) * np.exp(x)
        k2 = h * (3 + (x + h/2)) * np.exp(x + h/2)
        k3 = h * (3 + (x + h/2)) * np.exp(x + h/2)
        k4 = h * (3 + (x + h)) * np.exp(x + h)
        f_double_prime_val += (k1 + 2*k2 + 2*k3 + k4)/6
    
    return x_values, f_prime_approx, f_double_prime_approx

x0 = 1.5
x_end = 2.5
h = 0.1

x_values, f_prime_approx, f_double_prime_approx = runge_kutta4(f_prime, f_double_prime, x0, x_end, h)

print("x-values\tf'(x) Approximation\tf''(x) Approximation")
for x, fp, fpp in zip(x_values, f_prime_approx, f_double_prime_approx):
    print(f"{x:.1f}\t\t{fp:.4f}\t\t\t{fpp:.4f}")