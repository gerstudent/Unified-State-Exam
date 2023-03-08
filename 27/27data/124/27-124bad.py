from math import ceil

with open( '27.txt' ) as F:
  N, K, V, M = map( int, F.readline().split() )
  data = []
  for i in range(N):
    pos, volume = map( int, F.readline().split() )
    turns = ceil( volume / V )
    data.append( (pos, turns) )

bestPos = maxTotal = None

for i in range(N):
  pos1 = data[i][0]
  total = 0
  for j in range(N):
    pos2, vol = data[j]
    dist = min( abs(pos1-pos2), K-abs(pos1-pos2) )
    if dist <= M:
      total += vol
  if maxTotal == None or total > maxTotal:
    maxTotal = total
    bestPos = pos1
  print( pos1, total )

print( bestPos, maxTotal )
