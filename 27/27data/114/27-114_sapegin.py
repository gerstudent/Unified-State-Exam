# Автор: А. Сапегин

def factor(n):
    res = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.add(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.add(n)
    return res


with open("27-114a.txt") as f:
    N = int(f.readline())

    maxl = 0
    l = {}

    for i in range(N):
        x = int(f.readline())
        x = factor(x)
        for j in x:
            if j in l.keys():
                l[j] += 1
            else:
                l[j] = 1
        t = sorted(l.keys())
        for j in t:
            if j not in x:
                maxl = max(maxl, l[j])
                l.pop(j)

    maxl = max(maxl, max(l.values()))

print(maxl)