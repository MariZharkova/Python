
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# F−n = (−1)n+1Fn.


k = int(input('Введите число k = ' ))
f = list()
def fib(i):
    if i == 0:
        return 0
    elif i == 1 or i==2 or i==-1:
        return 1
    elif i == -2:
        return -1 
    elif i < 0:
        return (fib(i + 2)  - fib(i + 1))
    else:
        return (fib(i - 1) + fib(i - 2))
for m in range(-k, k+1):
    f.append (fib(m))
print (f)




