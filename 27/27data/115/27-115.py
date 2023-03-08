with open("27-115b.txt") as F:
  N = int( F.readline() )
  data = {}
  for i in range(N):
    x = int(F.readline())
    if data.get(x, 0) < 2:
      data[x] = data.get(x, 0) + 1

print( ( 1 + sum(data.values()) ) // 2 )


