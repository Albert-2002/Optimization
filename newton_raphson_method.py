"""Roots of a polynomial or transcendental equation using the newton raphson method."""

import sympy as sp
from scipy.optimize import newton

# Step 1: Symbolic definition
x = sp.symbols('x')
f_expr = x**2 + 5*x + sp.cos(x)  # Example polynomial

# Step 2: Symbolic derivative
df_expr = sp.diff(f_expr, x)

# Step 3: Convert to callable functions for SciPy
f_num = sp.lambdify(x, f_expr, 'math')
df_num = sp.lambdify(x, df_expr, 'math')

# Step 4: Newton–Raphson using SciPy
root1 = newton(f_num, x0=0.2, fprime=df_num, tol=1e-6)
print(f"Root near #1: {root1:.8f}")
