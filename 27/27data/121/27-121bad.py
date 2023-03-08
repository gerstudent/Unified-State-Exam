with open('27-121a.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

sMax = 0
for i in range(N-1):
  s = [0, 0]
  for j in range(i, N):
    s[j%2] += data[j]
    if s[0] == s[1] and 2*s[0] > sMax:
      sMax = 2*s[0]

print( sMax )