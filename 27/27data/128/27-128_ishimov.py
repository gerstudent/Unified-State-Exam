# Автор: М. Ишимов

with open('27-128b.txt') as f:
  n, m = map(int, f.readline().split())
  a = [int(f.readline()) for i in range(n)] * 2
m = (m + 2) // 3
people = [ sum(a[m:n-m+1]) ]
for i in range(1,n):
    people += [ people[-1] - a[(i+m-1) % n] + a[(i+n-m) % n] ]
print(people.index(max(people)) * 3)