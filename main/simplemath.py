import math

def f_me(x):
    if type(x) is not float and type(x) is not int or math.isinf(x) or x is None:
        return None
    return 25 * x + 10 # changeme
