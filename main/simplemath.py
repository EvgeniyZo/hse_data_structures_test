
def f_me(x):
    if not isinstance(x, (int, float)) or isinstance(x, bool) or x in {float("inf"), float("-inf")}:
        return None
    return 25 * x + 10
