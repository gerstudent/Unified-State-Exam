with open('27-109a.txt') as F:
  N = int(F.readline())
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
  return divs

data = [ primeDivs(x) for x in data ]

totalDivs = set()
for x in data:
  totalDivs = totalDivs.union( x )
K = len(totalDivs)

data = [ Counter( { d: 1 for d in divs } )
         for divs in data ]

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

