# Автор -  Муфаззалов Д.Ф.

f = open('27-124b.txt')
n, k, v, m = list(map(int, f.readline().split()))
a = [0] * k
for i in range(n):
    z, p = list(map(int, f.readline().split()))
    a[z % k] = p // v + (p % v > 0)
cm = sum(a)
if m < (k + 1) // 2 - 1:
    c = sum(a[:m * 2 + 1])
    cm = c if a[m] else 0
    for i in range(1, k):
        c += a[(i + m * 2) % k] - a[i - 1]
        if a[(i + m) % k]:
            cm = max(cm, c)
print(cm)
