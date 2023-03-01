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


# 5 (2)

def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}

    return sorted(d)


def fact(n):
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)

    return sorted(res)


for n in range(10, 135000):
    if len(divs(n)) == 0:
        continue
    else:
        d = max(divs(n))

    sm = sum(fact(n))
    q = int(str(sm)[::-1])

    if (n + d + q) > 202122:
        print(n, d + q)


# 16 (2)

def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}

    return sorted(d)


def check(n):
    d = divs(n)
    if sum(1 for i in d if i % 7 == 0) == 15:
        return n, max(d)


n = 10 ** 8
res = []
while len(res) < 5:
    k = check(n)
    if k:
        res.append(k)
    n += 1

n = 10 ** 9
while len(res) < 10:
    p = check(n)
    if p:
        res.append(p)
    n -= 1

for i in sorted(res):
    print(*i)


# 10 (2)

def check(s):
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            return False
    return True


for i in range(103, 10 ** 10, 103):
    s = str(i)
    if check(s):
        print(i, i // 103)

# 1 (1)

from fnmatch import fnmatch


def check(s):
    ln = len(s) // 2
    c2 = sum(map(int, s[:ln])) == sum(map(int, s[ln:]))
    c3 = '0' not in s
    return c2 and c3


for x in range(0, 10 ** 13, 519):
    s = str(x)
    if fnmatch(s, '32*54?123') and check(s):
        print(x, x // 519)

# 7 (1)

from fnmatch import fnmatch

cnt = 0
lst = []
for x in range(0, 17 * 10 ** 6, 161):
    if fnmatch(str(x), '*1?*?68*'):
        lst.append((x, x // 161))

for i in range(0, 17 * 10 ** 6, 500):
    print(*lst[i])

# 3 (1)

from fnmatch import fnmatch


def dec_to_seven(x):
    res = ''
    while x > 0:
        res = str(x % 7) + res
        x //= 7
    return res


for x in range(0, 10 ** 9, 333):
    num = str(dec_to_seven(x))
    if fnmatch(num, '?213*5664'):
        print(x, x // 333)

# 13 (2)

from fnmatch import fnmatch


def check(s):
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            return False
    return True


for x in range(0, 10 ** 9, 21):
    s = str(x)
    if check(s) and fnmatch(s, '1*5*9'):
        print(x, x // 21)

# 14 (2)

from fnmatch import fnmatch


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def divs(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if isprime(i):
                d.add(i)
            if isprime(x // i):
                d.add(x // i)

    return d


for n in range(4679000, 10 ** 9):
    d = divs(n)
    s = ''
    for i in sorted(d):
        s += str(i)
    if fnmatch(s, '27*39?') or fnmatch(s, '34*2?7'):
        print(n, max(d))


# 12 (2)

def isprime(x):
    return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))


def divs(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if isprime(i):
                d.add(i)
            if isprime(x // i):
                d.add(x // i)

    if len(d) != 0:
        return sorted(d)
    return 0


lst = []
cnt = 0
for i in range(121332132 + 1, 20222022, -1):
    div = divs(i)
    if div != 0:
        d = min(divs(i))
        if d > 999 and isprime(i) is False:
            lst.append((i, d))
            cnt += 1
            if cnt == 5:
                break

for i in lst:
    print(i[0], i[1])


# 6(2)

def check(lst):
    dif = lst[1] - lst[0]
    for i in range(2, len(lst)):
        if abs(lst[i] - lst[i - 1]) != dif:
            return False
    return True


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if isprime(i):
                d.add(i)
            if isprime(n // i):
                d.add(n // i)
    return sorted(d)


lst = []
for i in range(100000, 500000 + 1):
    d = divs(i)
    if len(d) > 3:
        if check(d):
            dif = abs(d[1] - d[0])
            lst.append((i, len(d) * dif))

for i in lst:
    print(i[0], i[1])

