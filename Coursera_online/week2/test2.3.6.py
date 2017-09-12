# За скільки днів спортсмен пробіжить задану к-сть км
x = int(input())
y = int(input())
i = 1
if x >= y:
    print(i)
else:
    while i != 0:
        x = (x + (x * 10 / 100))
        i = i + 1
        if x >= y:
            break
    print(i)
