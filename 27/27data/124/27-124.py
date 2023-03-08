from math import ceil

with open( '27-124b.txt' ) as F:
  N, K, V, M = map( int, F.readline().split() )
  data = [0]*K
  shift = None
  for i in range(N):
    pos, volume = map( int, F.readline().split() )
    if shift == None: shift = pos
    packs = ceil( volume / V )
    data[pos - shift] = packs

# предполагается, что 2*M < K
midPos1 = M
midPos2 = K - M - 1
sMinus = sum( data[midPos1+1:midPos2+1] )

#print( shift, midPos1, midPos2, sMinus )

bestPos, minUnavailable = shift, sMinus
for i in range(1,len(data)):
  midPos1 = (midPos1 + 1) % K
  midPos2 = (midPos2 + 1) % K
  sMinus += data[midPos2] - data[midPos1]
  #print( i + shift, midPos2, midPos1, sMinus )
  if data[i] > 0 and sMinus < minUnavailable:
    minUnavailable, bestPos = sMinus, i + shift

print( bestPos, sum(data) - minUnavailable )
