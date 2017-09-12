# Количество элементов, равных максимуму
n = int(input())
maxN = -1000000000
i = 0
while n != 0:
    n = int(input())
    if n != 0 and maxN < n:
        maxN = n
        i = 1
    elif maxN > n:
        continue
    elif n != 0 and maxN == n:
        i += 1
    # n = int(input())
print(i)
