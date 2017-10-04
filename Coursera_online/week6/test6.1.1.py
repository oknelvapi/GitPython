# Отсортируйте данный массив, используя встроенную сортировку.
n = int(input())
x = list(map(int, input().split()))
# a = range(1, n+1)
b = sorted(x)
print(*b)
