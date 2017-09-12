# Знайти мінімальний дільник числа n
from math import sqrt
x = int(input())


def minDivisor(x):
        i = 2
        while i <= sqrt(x) and x % i != 0:
            i += 1
        if i <= sqrt(x):
            return i
        else:
            return x


print(minDivisor(x))
