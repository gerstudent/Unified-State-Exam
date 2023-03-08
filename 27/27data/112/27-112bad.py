with open('27-112a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

def NOD( a, b ):
  while b:
    a, b = b, a % b
  return a
def manyNOD( a ):
  nod = NOD(a[0], a[1])
  for i in range(2,len(a)):
    nod = NOD( nod, a[i] )
  return nod

from itertools import combinations
maxNOD = 1
for selection in combinations(data, K):
  nod = manyNOD( selection )
  if nod > maxNOD:
    maxNOD = nod

print( maxNOD )

