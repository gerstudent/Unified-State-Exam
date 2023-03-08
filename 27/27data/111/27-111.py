with open('27-111b.txt') as F:
   N, X = map(int, F.readline().split())
   data = []
   for i in range(N):
      data.append( int(F.readline()) )

data.extend( data )

minCount = 10**10
start, end, s = 0, 0, data[0]
while s < X:
  end += 1
  s += data[end]

while start < N:
  while start < N and s > X:
    s -= data[start]
    start += 1
  if s == X:
    minCount = min( minCount, end - start + 1 )
  end += 1
  if end >= len(data): break
  s += data[end]

print( minCount )



