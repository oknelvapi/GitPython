# Штаб гражданской обороны Тридесятой области решил
# обновить план спасения на случай ядерной атаки.
# Известно, что все n селений Тридесятой области находятся
# вдоль одной прямой дороги.
# Вдоль дороги также расположены m бомбоубежищ,
# в которых жители селений могут укрыться на случай ядерной атаки.
# Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
# необходимо для каждого селения определить ближайшее к нему бомбоубежище.

cities = int(input())  # вводим кол-во поселений
citiesList = list(map(int, input().split()))  # расстояние от начала дороги до i-го селения
toc = []  # список кортежей из расстояния i-го селения и его индекс
shelters = int(input())  # вводим кол-во бомбоубежищ
sheltersList = list(map(int, input().split()))  # расстояние от начала дороги до j-го бомбоуб.
tos = []  # список кортежей из расстояния j-го бомбоуб. и его индекс
indS = []  # вывод списка номеров бомбоуб. для селений с 1го по i-тое

for i in range(cities):
    toc.append((int(citiesList[i]), i+1))
toc.sort()

for j in range(shelters):
    tos.append((int(sheltersList[j]), j+1))
tos.sort()

print(toc, tos, end='')