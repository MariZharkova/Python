
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i - 1)

N = int(input('Введите число N = ' ))

nums = list()
for m in range (1, N + 1):
    nums.append(factorial(m))
print(nums)
 

