from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return f(n - 2) + n - 2
    if n % 2 == 1:
        return f(n + 2) + n + 2


cnt = 0
for n in range(1, 1000):
    try:
        n1 = f(n) // 10000
        if 1 <= n1 <= 9:
            cnt += 1
    except RecursionError:
        print("fail")

print(cnt)
