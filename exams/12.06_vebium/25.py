def isPrime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def e(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}

    ans = list(i for i in d if isPrime(i))
    if len(ans) >= 2:
        return max(ans) - min(ans)
    else:
        return 0


for i in range(22800, 30000):
    if e(i) % 47 == 17:
        print(i, e(i))
