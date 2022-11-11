cache = {}


def f(n):
    if n not in cache:
        if n == 1:
            cache[n] = 2
        if n > 1:
            cache[n] = 2 * f(n - 1)
    return cache[n]


print(f(1900) // (2 ** 1890))
