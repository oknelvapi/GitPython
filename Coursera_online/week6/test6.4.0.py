# Сортировка подсчетом

marks = map(int, input().split())
cntMarks = [0] * 11
for mark in marks:
    cntMarks[mark] += 1
for nowMark in range(11):
    print((str(nowMark) + ' ') * cntMarks[nowMark], end='')

# Или:
# myList = list(map(int, input().split()))
# grades = [0] * 11
# for now in myList:
# 	grades[now] += 1
# for grade in range (len(grades)):
# 	for i in range(grades[grade]):
# 		print(grade, end= ' ')