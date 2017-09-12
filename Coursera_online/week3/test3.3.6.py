# Поміняти слова місцями
n = str(input())
f = n.find(' ')
first = n[:f]
second = n[f+1:]
print(second, first)
