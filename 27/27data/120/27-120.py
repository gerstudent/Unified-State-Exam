with open("27-120b.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

count = 0
triple = [0]*3
boundary = 0
for i in range(N):
  triple = triple[1:] + [data[i]]
  if triple.count(1) == 3:
    boundary = i - 1
  count += i - boundary + 1

print( count )