# Четные индексы
evenInd = list(map(int, input().split()))
print(' '.join(map(str, evenInd[0::2])))
