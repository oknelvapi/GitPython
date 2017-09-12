# Сума введеної послідовності
num = int(input())
numSum = 0
i = 1
while num != 0:
    numSum += num
    num = int(input())
    i += 1
print(numSum)
