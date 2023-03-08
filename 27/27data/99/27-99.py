with open("27-99b.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

midPos1 = N//2
midPos2 = N//2 if N % 2 == 0 else N//2+1
s, left, right = 0, data[0], 0
for i, d in enumerate(data):
  if i <= midPos1:
    s += data[i]*i
    if i > 0: right += data[i]
  else:
    s += data[i]*(N-i)
    if i > midPos2: left += data[i]

#print( 0, s, left, right )

bestPos, minSum = 0, s
for i in range(1,len(data)):
  s += left - right
  midPos1 = (midPos1 + 1) % N
  midPos2 = (midPos2 + 1) % N
  left += data[i] - data[midPos2]
  right += data[midPos1] - data[i]
  #print( i, s, left, right )
  if s < minSum:
    minSum, bestPos = s, i

print( bestPos + 1 )
