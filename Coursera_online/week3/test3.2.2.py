# Ціна товару. Записати окремо грн і копійки
n = float(input())
hrn = int(n)
kop = round(100 * (n % int(n)))
print(hrn, kop)
