with open('27-111b.txt') as F:
   N, X = map(int, F.readline().split())
   data = []
   for i in range(N):
      data.append( int(F.readline()) )

data.extend( data )

minCount = 10**10
for i in range(N):
  s, j = 0, i
  while j < 2*N and s < X:
    s += data[j]
    j += 1
  count = j - i
  if s == X and count < minCount:
    minCount = count

print( minCount )

