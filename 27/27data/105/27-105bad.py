with open("27.txt") as F:
  N, R = map(int, F.readline().split())
  data = [ float(F.readline()) for i in range(N) ]

minSum = bestPos = None
for i in range(N):
  s = 0
  for k in range(N//2+1):
    p1 = (i - k + N) % N
    p2 = (i + k) % N
    s += data[p1]*k*k
    if p1 != p2: s += data[p2]*k*k
  print( i+1, s*R*R )
  if not minSum or s < minSum:
    bestPos, minSum = i, s

print( 'Ответ:', bestPos+1, minSum*R*R )
