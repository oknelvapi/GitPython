h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
startSec = h1*3600 + m1*60 + s1
finishSec = h2*3600 + m2*60 + s2
print(finishSec - startSec)
