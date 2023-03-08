# Автор: А. Богданов

n, *a = map(int, open("27.txt"))

s = [0,0]
d = {0:0}
smax = 0
for i in range(n):
  s[i % 2] += a[i]
  r = s[0] - s[1]
  if r not in d:
    d[r] = sum(s)
  else:
    smax = max(smax,sum(s) - d[r])
print(smax)

