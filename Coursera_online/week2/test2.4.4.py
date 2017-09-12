# Довжина (кількість) парних чисел в послідовності
num = int(input())
i = 1
if num % 2 == 0:
    while num != 0:
        num = int(input())
        if num % 2 != 0:
            continue
        i += 1
    print(i - 1)
else:
    while num != 0:
        num = int(input())
        if num % 2 != 0:
            continue
        i += 1
    print(i - 2)
