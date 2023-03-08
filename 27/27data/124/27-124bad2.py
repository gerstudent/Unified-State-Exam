from math import ceil

with open( '27-124a.txt' ) as F:
  N, K, V, M = map( int, F.readline().split() )
  data = [0]*K
  shift = None
  for i in range(N):
    pos, volume = map( int, F.readline().split() )
    if shift == None: shift = pos
    turns = ceil( volume / V )
    data[pos - shift] = turns

def getTotal( pos ):
  total = 0
  for i in range(K):
    if data[i]:
      dist = min( abs(i-pos), K-abs(i-pos) )
      if dist <= M:
        total += data[i]
  return total

bestPos = maxTotal = None
for pos in range(K):
  if not data[pos]: continue
  total = getTotal(pos)
  if not maxTotal or total > maxTotal:
    maxTotal = total
    bestPos = pos + shift

print( bestPos, maxTotal )
