from math import ceil

with open('27-122a.txt') as F:
  N, V = map( int, F.readline().split() )
  data = []
  for i in range(N):
    pos, probs = map( int, F.readline().split() )
    data.append( (pos, ceil(probs/V)) )
  data.sort()

minSum = None
for i in range(N):
  s = 0
  for j in range(N):
    s += abs(data[i][0] - data[j][0]) * data[j][1]
  if minSum == None or s < minSum:
    minSum = s

print( minSum )