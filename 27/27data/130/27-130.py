with open('27-130bb.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

L = ((N // 2) - 1) // 2
pos1, pos2 = 0, N//2
minCost = sum( (data[pos1+i] + data[pos1-i])*i
             for i in range(L+1) ) \
        + sum( (data[(pos2+i)%N] + data[pos2-i])*i
             for i in range(L+1) )

# считаем разницу между cost[1] и cost[0]
diff = - L*(data[pos1-L] + data[pos2-L])
diff += sum( data[pos1-i]+data[pos2-i] for i in range(L) )
diff -= sum( data[pos1+1+i]+data[(pos2+1+i)%N] for i in range(L) )
diff += L*(data[pos1+1+L] + data[(pos2+1+L)%N])

cost = minCost
for pos1 in range(1,N//2):
  pos2 = N//2 + pos1
  cost += diff
  minCost = min( minCost, cost )
  # корректируем разницу между cost[pos1+1] и cost[pos1]
  diff += L*(data[pos1-1-L] + data[pos2-1-L])
  diff -= (L+1)*(data[pos1-1-L+1] + data[pos2-1-L+1])
  diff += 2*(data[pos1] + data[pos2])
  diff -= (L+1)*(data[pos1+L] + data[(pos2+L)%N])
  diff += L*(data[pos1+1+L] + data[(pos2+1+L)%N])

print( minCost )

# 69572

