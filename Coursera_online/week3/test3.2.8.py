# Квадратне рівняння
import math
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
eps = 5 * 10**-7
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 + eps < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif d == 0:
    x = -b/(2*a)
    print(x)
else:
    print()
