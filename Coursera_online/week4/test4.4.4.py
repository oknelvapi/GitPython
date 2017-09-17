# Швидке зведення у степінь aⁿ=a⋅aⁿ⁻¹


def power(a, n):
    if n == 0:
        return 1
    else:
        if n % 2 != 0:
            return a * power(a, n - 1)
        return power(a**2, n/2)

    # else:
    #     if n % 2 == 0:
    #         return 1/ (a * power(a, n / 2))


a = float(input())
n = int(input())
print(power(a, n))
