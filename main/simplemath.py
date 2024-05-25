
def f_me(x):
    return 0 # changeme
    if not isinstance(x, (int, float)) or x in [float("inf"), float("-inf"), None]:
        return None

    return x * 25 + 10
