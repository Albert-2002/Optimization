"""Quadratic Equation Solver."""

def solve_quadratic(a,b,c):
    """
    Solves a quadratic equation ax^2 + bx + c = 0.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple:  A tuple containing the roots of the equation.
                Returns (root1, root2) for the 2 roots. Does
                not handle complex roots.
    """

    if a == 0:
        # If 'a' is 0, it's a linear equation, not quadratic
        if b == 0:
            return "No solution or infinite solutions (if c=0)"

        return (-c / b,) # Return as a tuple for consistency

    discriminant = (b**2) - (4 * a * c)

    if discriminant < 0:
        return "No real root exists!"

    root1 = (-b + (discriminant)**0.5) / (2 * a)
    root2 = (-b - (discriminant)**0.5) / (2 * a)

    return (root1,root2)

# Example Usage:
# Real distinct roots
print("Roots for x^2 - 5x + 6 = 0:", solve_quadratic(1, -5, 6))

# Real repeated root
print("Roots for x^2 + 4x + 4 = 0:", solve_quadratic(1, 4, 4))

# Complex roots
print("Roots for x^2 + 2x + 5 = 0:", solve_quadratic(1, 2, 5))

# Linear equation case
print("Roots for 0x^2 + 2x + 4 = 0:", solve_quadratic(0, 2, 4))
