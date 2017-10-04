#                  Слияние списков
# Даны два списка A и B упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С
# (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается.
# Использовать функцию sorted и метод sort запрещается.
a = list(map(int, input('Input first list: ').split()))
b = list(map(int, input('Input second list: ').split()))


def merge(a, b):
    c = []
    i = 0
    j = 0
    # k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
        if i == len(a):
            c.extend(b[j::])
        if j == len(b):
            c.extend(a[i::])
    return c


print(*merge(a, b))
