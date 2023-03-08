with open('27-121b.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

s = [0, 0]
sMax = 0
diffs = {}
for i in range(N):
  s[i%2] += data[i]
  if s[0] == s[1]:
    sMax = max( 2*s[0], sMax )
  else:
    d = s[0] - s[1]
    if d in diffs:
      sMax = max( s[0] + s[1] - diffs[d], sMax )
    else:
      diffs[d] = s[0] + s[1]

print( sMax )