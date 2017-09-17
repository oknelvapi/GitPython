# Розвернення послідовності в зворотньому напрямку


def reverse():
    n = int(input())
    if n != 0:
        reverse()
        print(n)


reverse()
