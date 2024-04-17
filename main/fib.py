def fibonacci(n):
  

  if n < 2:
    return n

  a1 = 1
  a2 = 1

  for i in range(3, n + 1):
    an = a1 + a2
    a1 = a2
    a2 = an

  return an


# Вычисление первых 10 чисел Фибоначчи
for i in range(10):
  print(fibonacci(i))
