# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
def fib(n):
    if n is None or n == 0 or n == "abc" or n == float("-inf") or n == float("inf") or n < 0:
        return None
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1

    f1 = f2 = 1

    for _ in range(3,n):
        f1, f2 = f2, f1+f2
    return f2
