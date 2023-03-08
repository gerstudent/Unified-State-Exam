# Автор: Е. Джобс

from functools import lru_cache
@lru_cache(None)
def factorization(x):
	for d in range(2, int(x**0.5)+1):
		if x % d == 0:
			nx, deg = x, 0
			while nx % d == 0:
				nx //= d
				deg += 1
			return {d: deg} | factorization(nx)
	return {} if x == 1 else {x: 1}

from collections import Counter
with open('27-108b.txt') as f:
	n, k = map(int, f.readline().split())
	m = [factorization(int(f.readline())) for _ in range(n)]

s = Counter()
mn = float('inf')
cl = st = 0
for c in m:
	s.update(c)
	cl += 1
	while len(s) >= k:
		mn = min(mn, cl)
		s -= Counter(m[st])
		st += 1
		cl -= 1
print(mn)