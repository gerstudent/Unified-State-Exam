F = open('27-100a.txt')
N, M = map(int, F.readline().split())
data = [int(x) for x in F.readlines()]
F.close()

count = 0
for i in range(N):
  p = 1
  for j in range(i,N):
    p *= data[j]
    if p % M != 0:
      count += 1
      #print( data[i:j+1] )

print( count )
