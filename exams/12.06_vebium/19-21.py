from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(20000)


def moves(h):
    return h + 1, h + 5, h * 6, h * 3


@lru_cache(None)
def g(h):
    if 62 <= h <= 100:
        return 'w'
    if h > 100:
        return 'p1'
    if any(g(x) == 'w' for x in moves(h)):
        return 'p1'
    if all(g(x) == 'p1' for x in moves(h)):
        return 'v1'
    if any(g(x) == 'v1' for x in moves(h)):
        return 'p2'
    if all(g(x) == 'p2' or g(x) == 'p1' for x in moves(h)):
        return 'v2'


ans19, ans20, ans21 = [], [], []
for s in range(61, 0, -1):
    if g(s) == 'v1':
        ans19.append((s, g(s)))
    if g(s) == 'p2':
        ans20.append((s, g(s)))
    if g(s) == 'v2':
        ans21.append((s, g(s)))

print(min(ans19), len(ans20), min(ans21), max(ans21), sep='\n')
