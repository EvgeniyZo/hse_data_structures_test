# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
import math
import numbers

cache = dict()

def fib(n):
    if (not isinstance(n, numbers.Number) or math.isinf(n) or n <= 0):
        return None
    if (n == 1):
        return 0
    if (n == 2 or n == 3):
        return 1
    if n in cache:
        return cache[n]
    num = fib(n - 1) + fib(n - 2)
    cache[n] = num
    
    return num
