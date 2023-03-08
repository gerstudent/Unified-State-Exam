F = open('27-102a.txt')
N = int(F.readline())
data = [int(x) for x in F.readlines()]
F.close()

M = 524288
count = 0
for i in range(N):
  p = 1
  for j in range(i,N):
    p *= data[j]
    if p % M != 0:
      count += 1
      #print( data[i:j+1] )

print( count )
