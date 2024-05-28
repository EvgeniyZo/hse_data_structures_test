def fib(n):
    if isinstance(n, int):
        if n == 1:
            return 0
        if n > 0:
            fib1 = fib2 = 1
            while (n-2) > 0:
                fib1, fib2 = fib2, fib1 + fib2
                n -= 1
            return fib1
    return None
