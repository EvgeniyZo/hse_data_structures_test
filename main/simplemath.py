-
def f_me(x):
    return 0 # changeme
    if isinstance(x, str):
        return None
    if x is None:
        return None
    if x == float("inf") or x == float("-inf"):
        return None

    if x == 0:
        return 10

    return x * 25 + 10
