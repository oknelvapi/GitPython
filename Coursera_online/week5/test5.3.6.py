# В списке все элементы различны.
#  Поменяйте местами минимальный и максимальный элемент этого списка.
# numLine = list(map(int, input().split()))
myList = list(map(int, input().split()))
newList = list(myList)
newList[myList.index(min(myList))] = max(myList)
newList[myList.index(max(myList))] = min(myList)
print(*newList)
