with open("27.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

minSum = bestPos = None
for pos in range(N):
  sum = 0
  for i in range(N):
    dist = min( abs(i-pos), N-abs(i-pos) )
    sum += data[i]*dist
  #print( pos+1, sum )
  if not minSum or sum < minSum:
    minSum = sum
    bestPos = pos

print( bestPos + 1, minSum )
