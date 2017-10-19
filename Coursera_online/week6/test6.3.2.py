# Отсортировать список участников по алфавиту

# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.

# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8')

a = []
fin = open('input.txt', 'r', encoding='utf8')
# print(fin.readlines())
fout = open('output.txt', 'w', encoding='utf8')
for line in fin:
#     # a.append(line.strip())
#     # a.sort()
      s = line.split()
      a.append((s[0], s[1], s[3]))
#       print(s, end='', file=fout)
# # fout = open('output.txt', 'w', encoding='utf8')
# # print(fin.readlines(), file=fout)
a.sort()
for i in a:
    print(*i, file=fout)
# print(*a)
# print(*a, end='', file=fout)
fin.close()
fout.close()
