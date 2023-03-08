from math import ceil

with open( '27-123a.txt' ) as F:
  N, K, V = map( int, F.readline().split() )
  data = []
  for i in range(N):
    pos, volume = map( int, F.readline().split() )
    turns = ceil( volume / V )
    data.append( (pos, turns) )

bestPos = minCost = None

for i in range(N):
  pos1 = data[i][0]
  cost = 0
  for j in range(N):
    pos2, vol = data[j]
    dist = min( abs(pos1-pos2), K-abs(pos1-pos2) )
    cost += dist*vol
  if minCost == None or cost < minCost:
    minCost = cost
    bestPos = pos1
  print( pos1, cost )

print( bestPos, minCost )


