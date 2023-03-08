with open("27-120a.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

count = 3 # для двух последних элементов
for i in range(N-2):
  triple = [0, data[i], data[i+1]]
  count += 2
  for j in range(i+2,N):
    triple = triple[1:] + [data[j]]
    if triple.count(1) > 2: break
    count += 1
  #print( count )

print( count )