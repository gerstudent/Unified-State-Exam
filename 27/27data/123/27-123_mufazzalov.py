# Автор Муфаззалов Д.Ф.

for s in ['27-123a.txt', '27-123b.txt']:
    f = open(s)
    n, k, v = map(int, f.readline().split())
    a, b, r = [0] * k, k // 2, k % 2
    for i in range(n):
        j, z = map(int, f.readline().split())
        a[j % k] = z // v + (z % v > 0)
    cmin = c = sum([a[i] * (2*b+r-abs(2*(i-b)-r))//2 for i in range(1, k)])
    d = a[0] + sum(a[b + 2:k]) - sum(a[1:b + 1])
    for i in range(1, k):
        c += d
        d += 2 * a[i] - a[(b + i) % k] - a[(b + i + r) % k]
        cmin = min(cmin, c)
    print(cmin)
