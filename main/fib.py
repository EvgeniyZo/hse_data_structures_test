# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
def fib(n):
    # Additinal conditions for test
    if not isinstance(n, int) or (n < 1):
        return None
    if (n == 1):
        return 0
        
    a = [0, 1] 
      
    for i in range(2, n): 
        a.append(a[i-1] + a[i-2]) 
      
    # for i in range(n): 
    #     print(a[i]) 
    
    return a[-1]
