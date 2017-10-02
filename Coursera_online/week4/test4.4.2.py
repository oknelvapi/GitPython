# Отрицательная степень


def power(a, n):
    if n == 0:
        return 1
    if n < 0:
        return a * 1 / power(a, abs(n)+1)
    return a * power(a, n-1)


a = int(input())
n = int(input())
print(power(a, n))
# ЗАДАЧА ВИКОНАНА НЕ ПРАВИЛЬНО!
