# Належність точки на площині до квадрату
def isBelong(x, y):
    return 1 >= x >= -1 and 1 >= y >= -1


x = float(input())
y = float(input())
if isBelong(x, y):
    print('YES')
else:
    print('NO')
