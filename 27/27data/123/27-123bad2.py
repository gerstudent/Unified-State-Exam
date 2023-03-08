from math import ceil

with open( '27-123a.txt' ) as F:
  N, K, V = map( int, F.readline().split() )
  data = [0]*K
  shift = None
  for i in range(N):
    pos, volume = map( int, F.readline().split() )
    if shift == None: shift = pos
    turns = ceil( volume / V )
    data[pos - shift] = turns

def getCost( pos ):
  cost = 0
  for i in range(K):
    if data[i]:
      dist = min( abs(i-pos), K-abs(i-pos) )
      cost += data[i]*dist
  return cost

bestPos = minCost = None
for pos in range(K):
  if not data[pos]: continue
  cost = getCost(pos)
  if not minCost or cost < minCost:
    minCost = cost
    bestPos = pos + shift

print( bestPos, minCost )


