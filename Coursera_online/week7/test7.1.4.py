# Встречалось ли число раньше
#
# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO,
# если не встречалось.
#
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
num_list = set()
num_input = list(map(int, input().split()))
for i in num_input:
    if i in num_list:
        print('YES')
    else:
        print('NO')
        num_list.add(i)
