# Количество слов в тексте
#
# Во входном файле записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
file_in = open('input.txt', 'r', encoding='utf8')
i = 0
for k in file_in:
    lines = file_in.readline()
    # print(lines)
    print(k)
    for n in k:
        i += 1
        # print(i)