# Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a, b = 3, 5

def stepen(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b < 0:
        return 1/a * stepen(a, b + 1) # случай для b < 0
    return a * stepen(a, b - 1)

print(stepen(a, b))

