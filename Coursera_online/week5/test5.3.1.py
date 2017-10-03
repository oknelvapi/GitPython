# Напишите программу, которая находит в массиве элемент,
# самый близкий по величине к данному числу
n = int(input())
a = list(map(int, input().split()))
x = int(input())
i = 0
diff = 9999
ans = a[0]
while i < n:
    nextX = abs(a[i] - x)
    if nextX < diff:
        ans = a[i]
        diff = nextX
    i += 1
print(ans)
