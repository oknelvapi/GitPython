a = int(input())
b = int(input())
c = int(input())
if c <= a and b <= a:
    print(a)
elif a <= b and c <= b:
    print(b)
else:
    print(c)
