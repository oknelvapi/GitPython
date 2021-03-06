# Системный администратор вспомнил, что давно не делал архива
# пользовательских файлов.
# Однако, объем диска, куда он может поместить архив, может быть
# меньше чем суммарный объем архивируемых файлов.
# Известно, какой объем занимают файлы каждого пользователя.
# Напишите программу, которая по заданной информации о пользователях и
# свободному объему на архивном диске
# определит максимальное число пользователей, чьи данные можно поместить в архив,
# при этом используя свободное место как можно более полно.
sn = list(map(int, input().split()))
i = 0
n = []
while i < sn[1]:
    a = int(input())
    n.append(a)
    i += 1
n.sort()
amount = sum(n)
while amount > sn[0]:
    amount -= n.pop()
    i -= 1
print(i)
