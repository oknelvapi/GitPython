# Последний максимум
# maxNum = -999999
# i = 0
# for num in list(map(int, input().split())):
#     if num >= maxNum:
#         maxNum = num
#     # maxMun = mun.find(maxNum)
#     print(max(num))
#     # indexMax = len(num)-1-maxMun
#     # print(indexMax)
# # print(maxNum)
myList = list(map(int, input().split()))
for i in range(len(myList)):
    if myList[i] == max(myList):
        maxL = myList[i]
        ind = i
print(maxL, i-1)
