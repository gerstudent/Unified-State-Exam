def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}

    return sorted(d)


def check(x):
    d = divs(x)
    res = []
    for i in d:
        if i % 10 == 7:
            res.append(i)
    return len(res) == 3


def mx(x):
    d = divs(x)
    res = []
    for i in d:
        if i % 7 == 0:
            res.append(i)
    if len(res) == 3:
        return max(res)


for i in range(550000, 550041):
    if check(i):
        mx = max(j for j in divs(i) if j % 10 == 7)
        print(i, mx)
