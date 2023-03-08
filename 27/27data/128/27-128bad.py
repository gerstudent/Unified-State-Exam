
with open('27-128a.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(x) for x in F ]

def dist( pos1, pos2 ):
  d = abs( pos1 - pos2 )
  return 3 * min( d, N-d )

iMax, maxCount = None, 0
for i in range(N):
  count = sum( data[j] for j in range(N)
               if dist( i, j ) >= M )
  if count > maxCount:
     iMax, maxCount = i, count

print( iMax*3, maxCount )

