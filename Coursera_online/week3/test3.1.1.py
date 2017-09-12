# Площа трикутника за трьома сторонами
from math import sqrt
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2  # p - периметр трикутника
s = sqrt(p * (p - a) * (p - b) * (p - c))  # формула Герона
print(s)
