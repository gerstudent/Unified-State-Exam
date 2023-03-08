with open('27-119b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

half = K // 2

s1 = s2 = 0
pos0 = -1
for i in range(K):
  if data[i] == 0: pos0 = i
  if   i < half: s1 += data[i]
  elif i > half: s2 += data[i]
count = 1 if pos0 >= 0 and s1 == s2 else 0

for i in range(K, N):
  if data[i] == 0: pos0 = i
  s1 += data[i-half-1] - data[i-K]
  s2 += data[i] - data[i-half]
  if pos0 > i-K and s1 == s2:
    count += 1

print(count)