with open("27-118b.txt") as F:
  N, K, D = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

count = 0
for i in range(N):
  if data[i] == 0: continue
  num0 = 0
  for j in range(i+1, N):
    if data[j] == 0: num0 += 1
    elif num0 % K == 0 and (data[i] + data[j]) % D == 0:
      count += 1
      #print( data[i:j+1] )

print( count )
