def fib(n):
    if n == None or n == 0 or n == "abc" or n == float("-inf") or n == float("inf") or n < 0:
        return None
    if n == 1:
         return 0
    if n == 2 or n == 3:
         return 1
    
    fib1 = fib2 = 1

    for _ in range(3, n):
            fib1 , fib2 = fib2, fib1 + fib2
            
    return fib2
