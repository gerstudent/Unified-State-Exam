from collections import Counter
f = open('27-112b.txt')
n, k = map(int, f.readline().split())
p = dict(Counter(map(int, f.readlines())))
m = max(p)
for i in range(m, 0, -1):
    if sum([p.get(i * j, 0) for j in range(1, m // i + 1)]) >= k:
        print(i)
        break