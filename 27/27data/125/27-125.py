
with open('27-125b.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for _ in range(N) ]

total = sum(data)
half = total / 2
minCapacity, bestWay = None, None
data += data

def refreshResults():
  global pos, sumA, minCapacity, bestWay
  curCapacity = max( sumA, total-sumA )
  if sumA > total-sumA:
    stepBackCapacity = max( sumA-data[pos], total-sumA+data[pos] )
    if stepBackCapacity < curCapacity:
      curCapacity = stepBackCapacity
      sumA -= data[pos]
      pos -= 1
  curWay = min( [ pos-startPos, N-2-(pos-startPos) ] )
  # print( startPos, curCapacity, pos-startPos, N-2-(pos-startPos) )
  if minCapacity == None or curCapacity < minCapacity or\
     (curCapacity == minCapacity and curWay < bestWay):
    minCapacity = curCapacity
    bestWay = curWay
    # print( startPos, minCapacity, bestWay )

startPos = 0
pos, sumA = startPos-1, 0
while sumA < half:
  pos += 1
  sumA += data[pos]
refreshResults()

for startPos in range(1,N):
  sumA -= data[startPos-1]
  while sumA < half:
    pos += 1
    sumA += data[pos]
  refreshResults()

print( minCapacity, bestWay )