# чи є серед 3х чисел і парні й непарні
a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    if b % 2 != 0 or c % 2 != 0:
        print('YES')
    else:
        print('NO')
elif not 0 == a % 2:
    if b % 2 == 0 or c % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
