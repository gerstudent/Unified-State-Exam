# Автор: А. Кабанов

f = open('27-122a.txt')
n, v = map(int, f.readline().split())
a = []
for i in range(n):
  s, k = map(int, f.readline().split())
  # кол-во сумок
  c = k//v if k % v == 0 else k//v + 1
  a.append( [s, c] )
a.sort()

ms = 10**20
for i in range(n):
  s = 0
  for j in range(n):
    s += abs(a[i][0]-a[j][0])*a[j][1]
  ms = min(ms, s)

print(ms)