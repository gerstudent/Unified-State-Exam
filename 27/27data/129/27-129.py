D = 13

with open('27-129b.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )

data += data

tails = [ [[] for i in range(D)] for _ in range(D) ]
totalSum = 0
maxSum = 0
for i in range(2*N):
  totalSum += data[i]
  tail = tails[i%D][totalSum%D]
  if tail:
    for iTail, sumTail in tail[:]:
      if i - iTail <= N:
        maxSum = max( maxSum, totalSum - sumTail )
        break
      else:
        tail.remove( (iTail, sumTail) )
  tail.append( (i, totalSum) )

print( maxSum )
