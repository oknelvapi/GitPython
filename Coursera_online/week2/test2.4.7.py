# Вивести друге максимальне число в послідовності
n = int(input())
max1 = 0
max2 = n
while n != 0:
    if n != 0 and n >= max1:
        max2 = max1
        max1 = n
    elif max1 > n > max2:
        max2 = n
    n = int(input())
print(max2)
