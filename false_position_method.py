"""Find roots of polynomial or transcendental functions using the false position algorithm."""

import math

def f_1(x):
    """
    Example trigonometric transcendental function.

    Args:
        x (float): x-axis point value.

    Returns:
        float: Corresponding y-axis function value.
    """

    return float(x**2 + 5*x + math.cos(x))

def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    """
    Approximate root of polynomial or transcendental function by the method of false position.

    Args:
        f : A polynomial or transcendental function.
        a, b (float): Initial interval endpoints. (f(a) and f(b) must have opposite signs)
        tol (float): Tolerance for stopping. (default 1e-6)
        max_iter (int): Maximum number of iterations.

    Returns:
        xr (float): A root approximate of the function for an appropriate interval.
    """

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    for i in range(max_iter):
        # False-Position Formula
        xr = b - fb * (a - b) / (fa - fb)
        fxr = f(xr)

        # Debug info
        print(f"Iter {i+1}: a={a:.6f}, b={b:.6f}, xr={xr:.6f}, f(xr)={fxr:.6f}")

        if abs(fxr) < tol:  # root found
            return xr

        # Update interval
        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

    return xr

# Root in (0, 1)
root1 = regula_falsi(f_1, -5, -4, tol=1e-6)
print(f"Root in (-5,-4): {root1:.6f}")
print("\n")
# Root in (1, 2)
root2 = regula_falsi(f_1, -1, 0, tol=1e-6)
print(f"Root in (-1,0): {root2:.6f}")
