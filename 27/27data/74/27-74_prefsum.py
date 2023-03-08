# Автор: А. Богданов

f = open('27-74b.txt')

n = int(f.readline())
k = 20
a = [0]
for s in f:
  a += [a[-1]+int(s)]

c = 0
for i in range(n):
  for j in range(i+1,min(i+k+1,n)):
    if (a[j]-a[i])%39==0:
      c += 1

print(c)

