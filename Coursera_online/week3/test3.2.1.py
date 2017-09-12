# Дано положительное действительное число X. Выведите его дробную часть
n = float(input())
if int(n) == 0:
    nn = (n+1) % 1
else:
    nn = n % int(n)
print(nn)
