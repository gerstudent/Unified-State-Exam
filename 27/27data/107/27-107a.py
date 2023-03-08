F = open("27-107b.txt")
N = int(F.readline())

data = []
for i in range(N):
  s, f = map(int, F.readline().split())
  data.append( (s, f) )

data.sort( key = lambda x: x[1] )

lastPos, count = -1, 0
for s, f in data:
  if s > lastPos:
     lastPos = f
     count += 1

print( count )


