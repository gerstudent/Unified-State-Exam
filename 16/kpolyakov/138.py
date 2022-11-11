cache = {}


def f(n):
    if n not in cache:
        if n < 4:
            cache[n] = 1
        if n > 3 and n % 2 == 1:
            cache[n] = n
        if n > 3 and n % 2 == 0:
            cache[n] = f(n - 1) + f(n - 2) + f(n - 3)
    return cache[n]


print(f(2254) - f(2252))
