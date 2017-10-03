# Найдите количество положительных элементов в данном списке
pos = 0
for evenEl in input().split():
    if int(evenEl) > 0:
        pos += 1
print(pos)
