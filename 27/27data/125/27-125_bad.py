
with open('27-125a.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for _ in range(N) ]

total = sum(data)
half = total / 2
minCapacity, bestWay = None, None
data += data
for startPos in range(N):
  pos, sumA = startPos-1, 0
  while sumA < half:
    pos += 1
    sumA += data[pos]
    # print( '+', sumA, data[pos])
  curCapacity = max( sumA, total-sumA )
  if sumA > total-sumA:
    stepBackCapacity = max( sumA-data[pos], total-sumA+data[pos] )
    if stepBackCapacity < curCapacity:
      curCapacity = stepBackCapacity
      pos -= 1
  curWay = min( [ pos-startPos, N-2-(pos-startPos) ] )
  # print( startPos, curCapacity, pos-startPos, N-2-(pos-startPos) )
  if minCapacity == None or curCapacity < minCapacity or\
     (curCapacity == minCapacity and curWay < bestWay):
    minCapacity = curCapacity
    bestWay = curWay

print( minCapacity, bestWay )



