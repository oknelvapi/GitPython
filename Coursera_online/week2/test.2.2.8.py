# В'язень замку Іф
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if d >= a or d >= b or d >= c:
    if e >= a or e >= b or e >= c:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
