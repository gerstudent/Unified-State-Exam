with open("27-116b.txt") as F:
  N, K, D = map(int, F.readline().split())
  data = [ int(F.readline()) for i in range(N) ]

totalSum = sum(data)

count = 0
for i in range(N):
  s = 0
  for j in range(i,N):
    s += data[j]
    if s % K == 0 and (totalSum - s) % D == 0:
      count += 1

print( count )
