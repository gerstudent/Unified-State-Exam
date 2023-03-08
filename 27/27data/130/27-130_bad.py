with open('27a.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

L = ((N // 2) - 1) // 2
minCost = float('inf')
for pos1 in range(N // 2):
  pos2 = pos1 + N // 2
  print( pos1, end=" " )
  cost = sum( (data[pos1+i] + data[pos1-i])*i
               for i in range(L+1) )
  cost += sum( (data[(pos2+i)%N] + data[pos2-i])*i
                for i in range(L+1) )
  print( '>', cost )
  minCost = min( minCost, cost )

print( minCost )

# 69572

