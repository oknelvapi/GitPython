# упорядкувати три числа за зростанням
a = int(input())
b = int(input())
c = int(input())
if c <= b <= a:
    a, b, c = c, b, a
    print(a, b, c)
elif c <= a <= b:
    a, b, c = c, a, b
    print(a, b, c)
elif b <= a <= c:
    a, b, c = b, a, c
    print(a, b, c)
elif b <= c <= a:
    a, b, c = b, c, a
    print(a, b, c)
elif a <= c <= b:
    a, b, c = a, c, b
    print(a, b, c)
else:
    print(a, b, c)
