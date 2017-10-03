# Выведите все четные элементы списка
for evenEl in map(int, input().split()):
    if not int(evenEl) % 2 != 0:
        print(evenEl, end=' ')
