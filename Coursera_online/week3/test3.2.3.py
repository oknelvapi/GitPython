# Округлення по мат. правилам (1-4 --> 0, 5-9 ---> 1)
from math import floor, ceil
n = float(input())
nn = int(10*(n % int(n)))
if nn >= 5:
    print(ceil(n))
else:
    print(floor(n))
