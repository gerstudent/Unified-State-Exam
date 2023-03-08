with open('27-108b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

from collections import Counter

def primeDivs( n ):
  divs = set()
  d = 2
  while d <= n and n > 1:
    while n % d == 0:
      divs.add( d )
      n //= d
    d += 1
  return Counter( { d: 1 for d in divs } )

data = [ primeDivs(x) for x in data ]

minLen = 10**10
divSet = Counter()
tail = 0
for i, itemDivSet in enumerate(data):
  divSet += itemDivSet
  while len(divSet) >= K:
    L = i - tail + 1
    if L < minLen: minLen = L
    divSet -= data[tail]
    tail += 1

print( minLen )

