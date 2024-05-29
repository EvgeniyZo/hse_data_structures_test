# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
def fib(n):
    if isinstance(n, int):
        if n == 1:
            return 0
        elif n > 0:
            fib1 = 0
            fib2 = 1
            i = 0
            while i < n - 2:
                fib_sum = fib1 + fib2
                fib1 = fib2
                fib2 = fib_sum
                i = i + 1
            return fib2
        else:
            return None
    else:
        return None
