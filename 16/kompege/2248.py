from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + f(n / 3)
    if n % 3 != 0:
        return n + f(n + 3)


cnt = 0
for n in range(1, 1000):
    try:
        if f(n) > 100:
            print(n)
            break
    except RecursionError:
        print("fail")
