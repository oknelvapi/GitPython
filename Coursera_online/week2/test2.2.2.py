# Визначити чи лежать задані точки в одній коорд. площині
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0 < x2:
    if y1 > 0 < y2:
        print('YES')
    elif y1 < 0 > y2:
        print('YES')
    else:
        print('NO')
elif x1 < 0 > x2:
    if y1 > 0 < y2:
        print('YES')
    elif y1 < 0 > y2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
