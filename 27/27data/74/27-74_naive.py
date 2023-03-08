# Автор: А. Богданов

f = open('27-74b.txt')
n = int(f.readline())
a = list(int(s) for s in f)

d = 20
c = 0
for i in range(n):
  s = 0
  for j in range(i,min(n,i+d)):
    s += a[j]
    if s % 39 == 0:
      c += 1
print(c)
