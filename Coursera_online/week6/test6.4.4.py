# Результаты олимпиады
# В олимпиаде участвовало N человек.
# Каждый получил определенное количество баллов, при этом оказалось,
# что у всех участников разное число баллов. Упорядочите список
# участников олимпиады в порядке убывания набранных баллов.

# Формат ввода
# Программа получает на вход число участников олимпиады N.
# Далее идет N строк, в каждой строке записана фамилия участника,
# затем, через пробел, набранное им количество баллов.

# Формат вывода
# Выведите только фамилии в порядке убывания набранных баллов.


class Olimpian:
    name = ''
    rating = 0
p = []
number = int(input())
for i in range(number):
    n, r = input().split()
    r = int(r)
    competitor = Olimpian()
    competitor.name = n
    competitor.rating = r * (-1)
    p.append(competitor)


def make_tuple(member):
    return member.rating


p.sort(key=make_tuple)
for now in p:
    print(now.name)
