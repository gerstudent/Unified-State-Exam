F = open('27-100b.txt')
N, M = map(int, F.readline().split())
data = [int(x) for x in F.readlines()]
F.close()

count = 0
rCount = [0]*M
for x in data:
  rCountNew = [0]*M
  rCountNew[x % M] = 1
  if x % M: count += 1
  for r in range(1,M):
    if rCount[r]:
      rNew = (r*x) % M
      rCountNew[rNew] += rCount[r]
      if rNew:
        count += rCount[r]
  rCount = rCountNew[:]
  #print(x, count, [(r, rCount[r]) for r in range(M) if rCount[r] > 0])

print( count )

"""
count = 0
rCount = {}
for x in data:
  rCountNew = { (x % M): 1 }
  for r in range(1,M):
    if r in rCount:
      rNew = (r*x) % M
      rCountNew[rNew] = rCountNew.get(rNew, 0) + rCount[r]
  rCount = rCountNew.copy()
  for r in rCount:
    if r: count += rCount[r]
  #print(x, count, rCount)

print( count )
"""