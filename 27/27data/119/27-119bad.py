with open('27-119a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

half = K // 2

count = 0
for i in range(N-K+1):
  found0 = False
  chunk = data[i:i+K]
  if 0 in chunk and \
     sum(chunk[:half]) == sum(chunk[-half:]):
     count += 1

print(count)