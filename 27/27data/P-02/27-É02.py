f = open('27-r02.txt')
n = int(f.readline())

D = 12
k = [0]*D

xx = []
for i in range(n):
    x = int(f.readline())
    xx.append(x)
    k1 = k.copy()
    for i in range(D):
        k1[ (i+x) % D] +=k[i]
    k1[ x % D ]+=1
    k = k1.copy()
    print(x, k)
f.close()

print( k[0] )

from itertools import combinations
allSets = []
for k in range(1,n+1):
  allSets += combinations( xx, k )
allSets = [x for x in allSets if sum(x) % D == 0]
print( allSets )

