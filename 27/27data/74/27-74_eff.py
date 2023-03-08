# Автор: А. Богданов

f = open('27-74b.txt')
n = int(f.readline())

k = 20
t = [[-1]]+[[] for _ in range(38)]

s = c = 0
for i in range(n):
  s += int(f.readline())
  p = t[s % 39]
  while p and i - p[0] > k:
    p.pop(0)
  c += len(p)
  p += [i]
print(c)

