with open('27-108a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

def primeDivs( n ):
  divs = set()
  d = 2
  while d <= n and n > 1:
    while n % d == 0:
      divs.add( d )
      n //= d
    d += 1
  return divs

minLen = 10**10
for i in range(N):
  p = 1
  for j in range(i,N):
    p *= data[j]
    if len(primeDivs(p)) >= K and (j-i+1) < minLen:
       minLen = j - i + 1

print( minLen )

