with open('27-109a.txt') as F:
  N = int(F.readline())
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

minLen, maxCount = 10**10, 0
for i in range(N):
  p = 1
  for j in range(i,N):
    p *= data[j]
    count = len(primeDivs(p))
    if  count > maxCount or \
       (count == maxCount and (j-i+1) < minLen):
       maxCount = count
       minLen = j - i + 1

print( minLen )

