# Дан список чисел.
# Выведите все элементы списка, которые больше предыдущего элемента.
n = list(map(int, input().split()))
b = []
i = 0
while i < len(n)-1:
    if n[i] < n[i+1]:
        b.append(n[i+1])
    i += 1
print(*b)
