def f_me(x):
    if x is None:
        return None
    elif x == float("inf"):
        return None
    elif x == float("-inf"):
        return None
    elif isinstance(x, str):
        return None
    elif isinstance(x, int) or isinstance(x, float):
        return 25 * x + 10
