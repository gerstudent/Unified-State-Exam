# 16 (1)

from fnmatch import fnmatch

for x in range(161, 10 ** 8):
    if fnmatch(str(x), '12*4?65') and x % 161 == 0:
        print(x, x // 161)

# 11 (1)

from fnmatch import fnmatch

for x in range(206, 10 ** 8, 206):
    if fnmatch(str(x), '123*[13579][02468]56'):
        print(x, x // 206)

# 8 (1)

from fnmatch import fnmatch


def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}

    return sorted(d)


for x in range(1, 3163):
    n = x ** 2
    if fnmatch(str(n), '3*52?'):
        d = div(n)
        print(n, max(d))


# 14 (1)

def divs(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}

    return d


def mult(lst):
    res = 1
    for i in lst:
        res *= i
    return res


for i in range(10 ** 6, 10 ** 10):
    div = divs(i)
    if sum(div) % 2 != 0 and mult(div) % 2 != 0 and len(div) > 40:
        print(i, len(div))


# 12 (1)

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(9998, 10 ** 7, 9998):
    s = str(i)
    p = int(s[1:-1])
    if s[0] == '9' and isPrime(p):
        print(i, i // 9998)

# 13 (1)

import math


def divs(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}

    return sorted(d)


def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


for i in range(2 * 10 ** 6, 10 ** 7):
    d = divs(i)
    if sum(d) % 2 != 0 and math.prod(d) % 2 != 0 and len(d) > 30:
        print(i, max(c for c in d if isprime(c)))


# 3 (2)

def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def divs(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}

    return sorted(d)


n = 10 ** 8
cnt = 0
while cnt < 5:
    primes = [c for c in divs(n) if isprime(c)]
    chet = [c for c in divs(n) if c % 2 == 0]
    m = abs(sum(primes) - sum(chet))
    if len(primes) == len(chet):
        print(n, m)
        cnt += 1
    n += 1
