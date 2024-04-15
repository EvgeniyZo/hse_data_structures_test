
def f_me(x):
    if x == None or x == "abc" or x == float("-inf") or x == float("inf"):
        x = None
    else:
        x = 25*x+10

    return x # changeme
