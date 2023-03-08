from collections import Counter

f = open('27-115b.txt')
n = int(f.readline())
d = Counter(map(int, f))
print((1 + sum([min(2, d[j]) for j in d])) // 2)
