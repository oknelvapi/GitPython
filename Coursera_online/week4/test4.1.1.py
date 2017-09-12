# min з 4х чисел


def min4(a, b, c, d):
    x = min(a, b)
    y = min(c, d)
    z = min(x, y)
    return z

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
