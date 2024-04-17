# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
def fib(n):
	try:
		if n is None or abs(n) == float("inf") or n <= 0:
			return None
		
		if n <= 2:
			return n - 1
		if n == 3:
			return 1
	except:
		return None
	return fibonacci(n - 1, 1, 1)

def fibonacci(n, a, b):
	if n <= 3:
		return a + b
	return fibonacci(n - 1, b, a + b)