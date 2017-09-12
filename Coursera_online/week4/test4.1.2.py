# Відстань між точками на координатній площині
from math import sqrt


def distance(x1, y1, x2, y2):
    ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return ab


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
