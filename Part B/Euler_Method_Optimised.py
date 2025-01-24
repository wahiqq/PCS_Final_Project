import numpy as np

def f(x):
    """Calculate f(x) = x * e^x."""
    return x * np.exp(x)

def f_prime(x):
    """Calculate f'(x) = (1 + x) * e^x."""
    return (1 + x) * np.exp(x)

def f_double_prime(x):
    """Calculate f''(x) = (2 + x) * e^x."""
    return (2 + x) * np.exp(x)

def euler_method_optimized(f_prime, f_double_prime, x0, x_end, h):
    """Euler's method optimized for f'(x) and f''(x)."""
    if h <= 0:
        raise ValueError("Step size h must be positive.")
    if x_end < x0:
        raise ValueError("x_end must be greater than or equal to x0.")
    
    steps = int((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, steps)
    f_prime_approx = np.zeros(steps)
    f_double_prime_approx = np.zeros(steps)
    
    f_prime_val = f_prime(x0)
    f_double_prime_val = f_double_prime(x0)
    
    for i, x in enumerate(x_values):
        f_prime_approx[i] = f_prime_val
        f_double_prime_approx[i] = f_double_prime_val
        
        exp_x = np.exp(x)
        f_prime_val += h * f_double_prime_val
        f_double_prime_val += h * ((3 + x) * exp_x)
        
    return x_values, f_prime_approx, f_double_prime_approx

def test_functions():
    """Test f, f_prime, and f_double_prime."""
    x_test = 1.0
    assert np.isclose(f(x_test), x_test * np.exp(x_test)), "f(x) test failed."
    assert np.isclose(f_prime(x_test), (1 + x_test) * np.exp(x_test)), "f'(x) test failed."
    assert np.isclose(f_double_prime(x_test), (2 + x_test) * np.exp(x_test)), "f''(x) test failed."

def test_euler_method():
    """Test the Euler method approximation."""
    x0, x_end, h = 1.5, 2.5, 0.1
    x_values, f_prime_approx, f_double_prime_approx = euler_method_optimized(f_prime, f_double_prime, x0, x_end, h)
    
    assert len(x_values) == int((x_end - x0) / h) + 1, "Incorrect number of steps."
    
    for x, fp_approx, fpp_approx in zip(x_values, f_prime_approx, f_double_prime_approx):
        assert np.isfinite(fp_approx), "f'(x) approximation is not finite."
        assert np.isfinite(fpp_approx), "f''(x) approximation is not finite."

test_functions()
test_euler_method()

x0 = 1.5
x_end = 2.5
h = 0.1

x_values, f_prime_approx, f_double_prime_approx = euler_method_optimized(f_prime, f_double_prime, x0, x_end, h)

print("x-values\tf'(x) Approximation\tf''(x) Approximation")
for x, fp, fpp in zip(x_values, f_prime_approx, f_double_prime_approx):
    print(f"{x:.1f}\t\t{fp:.4f}\t\t\t{fpp:.4f}")
