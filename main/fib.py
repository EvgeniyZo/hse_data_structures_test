# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
def fib(n: int):
    if isinstance(n, str):
        return None
    if n is None:
        return None
    if n == 0:
        return None
    if n < 0:
        return None
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    if n == float("inf") or n == float("-inf"):
        return None

    n1 = 1
    n2 = 1

    res = 0

    for _ in range(3, n):
        res = n2 + n1

        n1 = n2
        n2 = res

    return res
