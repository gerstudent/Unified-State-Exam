with open("27-117b.txt") as F:
  N, D = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

M = 10000

M = max(data)

tailCount = [ [0]*D for i in range(M+1) ]

count = s = 0
for i in range(N):
  r = s % D
  count += tailCount[data[i]][r]
  if i > 0 and data[i] == data[i-1]: # пара одинаковых элементов
    count -= 1
  s += data[i]
  rNew = s % D
  tailCount[data[i]][rNew] += 1

print( count )
