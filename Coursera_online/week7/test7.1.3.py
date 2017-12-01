# Пересечение множеств
#
# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый,
# так и во второй список в порядке возрастания.
#
# Формат ввода
# Вводятся два списка целых чисел.
# Все числа каждого списка находятся на отдельной строке.
#
# Формат вывода
# Выведите ответ на задачу.
# Примечания: Ввод и вывод осуществлять с помощью файлов.
'''
# Перший варіант, не дуже вдалий
fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
a = []
for line in fin:
    a.append(line.split())
b = set(map(int, a[0]))
c = set(map(int, a[1]))
print(*sorted(b & c), file=fout)
fin.close()
fout.close()
'''''
# Другий варіант
fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
a = []
for s in fin:
    a.append(s.split())
b = set(a[0])
for i in range(1, len(a)):
    b = b & set(a[1])
print(*sorted(map(int, b)), file=fout)
fin.close()
fout.close()
#
'''''
f_in = open('input.txt', 'r', encoding='utf8')
f_out = open('output.txt', 'w', encoding='utf8')
i = 0
for s in f_in:
    if i == 0:
        b = set(s.split())
    else:
        b = b & set(s.split())
    i += 1
print(b)
print(*sorted(map(int, b)), file=f_out)
f_in.close()
f_out.close()
'''''