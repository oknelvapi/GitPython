# Буква "f" в рядку - перший і останній індекс
s = str(input())    # вводиться рядок
s999 = s[::-1]  # виводиться рядок навпаки
f = s.find('f') # щоб не викликати  щоразу, записуємо його у змінну
f1 = s999.find('f') # присвоюємо змінну для рядка навпаки
if f == -1: # якщо заданої букви в рядку нема - нічого не друкувати
    print()
# f - номер першої літери в рядку, f1 - номер останньої літери;
# якщо літера в рядку одна, то сума f+f1+1 дорівнюватиме
# довжині рядка len (1 плюсуємо, бо рахунок поч. з 0). Отже:
elif len(s) == (f + f1+1):
    print(f)
else:   # Коли літер 2 і більше, виводимо першу і останню літери
    print(f, len(s)-1-f1)
print(s[f:-1])
