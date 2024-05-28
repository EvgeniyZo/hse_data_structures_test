import math


def f_me(x):
    if isinstance(x, (int, float)):
        if not math.isinf(x):
            return x * 25 + 10
    return None

