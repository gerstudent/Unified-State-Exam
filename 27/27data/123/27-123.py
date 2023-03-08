from math import ceil

with open( '27-123b.txt' ) as F:
  N, K, V = map( int, F.readline().split() )
  data = [0]*K
  shift = None
  for i in range(N):
    pos, volume = map( int, F.readline().split() )
    if shift == None: shift = pos
    turns = ceil( volume / V )
    data[pos - shift] = turns

midPos1 = K//2
midPos2 = K//2 if K % 2 == 0 else K//2+1
s, left, right = 0, data[0], 0
for i, d in enumerate(data):
  if i <= midPos1:
    s += data[i]*i
    if i > 0: right += data[i]
  else:
    s += data[i]*(K-i)
    if i > midPos2: left += data[i]

#print( 0, s, left, right )

bestPos, minSum = shift, s
for i in range(1,len(data)):
  s += left - right
  midPos1 = (midPos1 + 1) % K
  midPos2 = (midPos2 + 1) % K
  left += data[i] - data[midPos2]
  right += data[midPos1] - data[i]
  #print( i, s, left, right )
  if data[i] > 0 and s < minSum:
    minSum, bestPos = s, i + shift

print( bestPos, minSum )
