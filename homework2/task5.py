
# Реализуйте алгоритм перемешивания списка.

import random

s = []
N = int(input('Введите число элементов N = ' ))

for i in range (N):
    s.append(random.randrange (-N, N))
print (s)
for k in range (N):
    m = random.randrange (0, N)
    n = random.randrange (0, N)
    tmp = s[n]
    s[n] = s[m]
    s[m] = tmp
print (s)