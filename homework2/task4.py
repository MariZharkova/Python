
#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на позициях a и b. 
# Значения N, a, b вводит пользователь с клавиатуры через пробел

import random
def get_numbers():
    while True:
        N, a, b = input ('Введите число элементов в списке N, позиции перемножаемых элементов из списка a и b = ' ).split ( )
        a = int (a)
        b = int (b)
        N = int (N)
        if a < 0 or b < 0 or N <= 0 or a >= N or b >= N:
            print ('Числа не удовлетворяют условию задачи. Повторите ввод.')
            continue
        return (N, a, b)

N, a, b = get_numbers()
s = [ ]
for i in range (N):
    s.append(random.randrange (-N, N+1))
print (s)
print (s[a]*s[b])


