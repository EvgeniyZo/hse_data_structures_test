
def f_me(x):
    if not isinstance(x, (int, float)) or x in [float("inf"), float("-inf"), None]:
        return None

    return x * 25 + 10
