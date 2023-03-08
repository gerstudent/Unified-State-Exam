with open("27-116b.txt") as F:
  N, K, D = map(int, F.readline().split())
  data = [ int(F.readline()) for i in range(N) ]

totalSum = sum(data)

tailCount = [ [0]*D for i in range(K) ]

count = 0
s = 0
for i in range(N):
  s += data[i]
  r, rRest = s % K, (totalSum-s) % D
  count += tailCount[r][D-rRest] if rRest > 0 else \
           tailCount[r][0]
  if r == 0 and rRest == 0:
    count += 1
  tailCount[r][s%D] += 1

print( count )
