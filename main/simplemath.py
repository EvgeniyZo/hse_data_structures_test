
def f_me(x):
    if isinstance(x, (int, float)) and abs(x) < float("inf"):
        return x * 25 + 10
    return None
