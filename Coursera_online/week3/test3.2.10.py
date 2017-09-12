# Система лінійних рівнянь
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
#  |ax + by = e
#  |cx + dy = f
delta = a * d - c * b
deltaX = e * d - f * b
deltaY = f * a - e * c
x = deltaX/delta
y = deltaY/delta
print(x, y)
