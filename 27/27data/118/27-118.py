with open("27-118a.txt") as F:
  N, K, D = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

tailCount = [[0]*D for i in range(K)]
count = num0 = 0
for i in range(N):
  if data[i] == 0:
    num0 += 1
  else:
    r = data[i] % D
    count += tailCount[num0 % K][D - r] if r > 0 else \
             tailCount[num0 % K][0]
    tailCount[num0 % K][r] += 1

print( count )
