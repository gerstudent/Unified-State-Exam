with open('27-112b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = {}
  M = 0
  for i in range(N):
    val = int(F.readline())
    data[val] = data.get(val, 0) + 1
    M = max(M, val)

maxNOD = 1
val = 1
while val <= M:
  n, count = val, 0
  while n <= 10**6 and count < K:
    count += data.get(n, 0)
    n += val
  if count >= K:
    maxNOD = val
  val += 1

print( maxNOD )

