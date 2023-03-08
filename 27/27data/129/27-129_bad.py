D = 13

with open('27-129b.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )

data += data

maxSum = 0
for i in range(N):
  for k in range(i+D,i+N,D):
    curSum = sum(data[i:k])
    if curSum % D == 0 and curSum > maxSum:
      maxSum = curSum

print( maxSum )
