# Типи трикутників
a = int(input())
b = int(input())
c = int(input())
if a + b > c > abs(a-b) or b + c > a > abs(c-b) or c + a > b > abs(c-a):
    if a <= c >= b:
        if (a**2 + b**2) < (c**2):
            print('obtuse')
        elif (a**2 + b**2) > (c**2):
            print('acute')
        elif (a**2 + b**2) == (c**2):
            print('rectangular')
        else:
            print('impossible')
    elif c <= b >= a:
        if (a ** 2 + c ** 2) < (b ** 2):
            print('obtuse')
        elif (a ** 2 + c ** 2) > (b ** 2):
            print('acute')
        elif (a ** 2 + c ** 2) == (b ** 2):
            print('rectangular')
        else:
            print('impossible')
    elif c <= a >= b:
        if (c ** 2 + b ** 2) < (a ** 2):
            print('obtuse')
        elif (c ** 2 + b ** 2) > (a ** 2):
            print('acute')
        elif (c ** 2 + b ** 2) == (a ** 2):
            print('rectangular')
        else:
            print('impossible')
    else:
        print('impossible')
else:
    print('impossible')
