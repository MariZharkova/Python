
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Решение:

def is_true (x, y, z):
    return (not (x or y or z)) == (not (x)) and (not (y)) and (not (z))


print (is_true (False, False, False))


