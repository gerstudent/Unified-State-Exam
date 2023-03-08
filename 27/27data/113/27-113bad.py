with open("27.txt") as F:
  N = int( F.readline() )
  data = [ int(F.readline()) for i in range(N) ]

tariff = { 1: 15, 11: 40, 21: 70 }

from functools import lru_cache
#@lru_cache
def minCost( fromPos = 0, paidUntil = 0 ):
  if fromPos >= N: return 0
  if data[fromPos] <= paidUntil:
    return minCost( fromPos+1, paidUntil )
  mi = None
  for count, money in tariff.items():
    cost = money + minCost( fromPos+1, data[fromPos]+count-1 )
    if not mi or cost < mi:
      mi = cost
  return mi

print( minCost() )


