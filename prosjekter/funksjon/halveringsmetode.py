def f(x):
    return (1/3*(x**3)+1/2*(x**2)-x-1)

def solve(a: float, b: float) -> float:
    """
    Solve f(x) = 0 using the bisection method.

    Parameters:
    ----------
    a (int): start of interval
    b (int): end of interval

    Return:
    -------
    (int): x-value where f(x) = 0
    """
    m = (a + b) / 2
    if abs(f(m)) < 0.01:
        return m
    
    if f(a) * f(m) < 0:
        return solve(a, m)
    else:
        return solve(m, b)
    
print(solve(-2, 2))