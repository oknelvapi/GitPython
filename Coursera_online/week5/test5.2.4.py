# Последний максимум
n = list(map(int, input().split()))
maxL = 99999
ind = 0
for i in range(len(n)):
    if n[i] == max(n):
        maxL = n[i]
        ind = i
print(maxL, ind)
