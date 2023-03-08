F = open('27-101b.txt')
N = map(int, F.readline().split())
data = [int(x) for x in F.readlines()]
F.close()

M = 858967 # = 79*83*131

pos = {}
d = 2
while M > 1:
  if M % d == 0:  # только для случая некратных простых делителей!
    pos[d] = -1
    M //= d
  d += 1

print(pos)

count = 0
for i, x in enumerate(data):
  for d in pos:
    if x % d == 0:
      pos[d] = i
  count += (i - min(pos.values()))

print( count )

