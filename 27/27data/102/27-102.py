F = open('27-102a.txt')
N = map(int, F.readline().split())
data = [int(x) for x in F.readlines()]
F.close()

M = 524288 # 2**19

pos = {}
d = 2
while M > 1:
  while M % d == 0:  # работает и для случая некратных простых делителей!
    pos[d] = pos.get(d, []) + [-1]
    M //= d
  d += 1

count = 0
for i, x in enumerate(data):
  for d in pos:
    while x % d == 0:
      pos[d].pop(0)
      pos[d].append(i)
      x //= d
  count += (i - min(min(pos.values())))

print( count )

