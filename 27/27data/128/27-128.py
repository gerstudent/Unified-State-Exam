fName = '27.txt'
fName = '27-128a.txt'
fName = '27-128b.txt'

with open(fName) as F:
  N, M = map( int, F.readline().split() )
  data = [ int(x) for x in F ]

from math import ceil

D = ceil( M / 3 )
L, R = N - D, D

count = sum( data[j] for j in range(R, L+1) )
iMax, maxCount = 0, count

for i in range(1, N):
  L = (L + 1) % N
  count += data[L] - data[R]
  R = (R + 1) % N
  if count > maxCount:
    iMax, maxCount = i, count

print( iMax*3, maxCount )
