with open("27-114b.txt") as F:
  N = int( F.readline() )
  data = [ int(F.readline()) for i in range(N) ]

def NOD( a, b ):
  while b:
    a, b = b, a % b
  return a

maxLen = 0
for i in range(N):
  L, d = 1, data[i]
  for j in range(i+1,N):
    d = NOD( d, data[j] )
    if d == 1: break
    L += 1
    if L > maxLen: maxLen = L

print( maxLen )