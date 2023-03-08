with open("27-117b.txt") as F:
  N, D = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

count = 0
for i in range(1,N-2):
  s = 0
  for j in range(i,N-1):
    s += data[j]
    if s % D == 0 and data[i-1] == data[j+1]:
       count += 1

print( count )