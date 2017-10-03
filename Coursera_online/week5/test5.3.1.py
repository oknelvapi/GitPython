# Напишите программу, которая находит в массиве элемент,
# самый близкий по величине к данному числу
n = int(input())
a = list(map(int, input().split()))
x = int(input())
i = 0
nextX = x
while i < len(a):
    # nextX = abs(a[i]-x)
    # if a[i] == x:
    #     print(x)
    if abs(a[i]-x) <= nextX:
        num = a[i]
        # print(nextX)
    i += 1
print(nextX)



