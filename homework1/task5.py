
#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Решение:

print ('Введите координаты точки A:')
x1 = int (input('x1 = ' ))
y1 = int (input('y1 = ' ))
print ('Введите координаты точки B:')
x2 = int (input('x2 = ' ))
y2 = int (input('y2 = ' ))

xmax = max (x1, x2)
xmin = min (x1, x2)
ymax = max (y1, y2)
ymin = min (y1, y2)

if ((x1 == x2) and (y1 == y2)):
    print ('0')
elif x1 == x2:
    print (ymax - ymin)
elif y1 == y2:
    print (xmax - xmin)
else:
    print (round (((((xmax - xmin)**2) + ((ymax - ymin)**2))**0.5), 2))
    
