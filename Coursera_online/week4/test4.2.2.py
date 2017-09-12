# Належність точки на площині до кола
def isPointInCircle(x, y, xc, yc, r):
    return (xc - x)**2 + (yc - y)**2 <= r**2
# Рівняння, де відстань від центру кола до його хорди має вигляд:
# (x0-x)**2+(y0-y)=r**2 - це означатиме, що якщо точка лежить в колі
# або на його межі, то відстань від неї до центру кола завжди буде
# меншою або рівною квадрату радіусу
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if isPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
