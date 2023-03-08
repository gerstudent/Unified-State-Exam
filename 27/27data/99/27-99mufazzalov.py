# Автор: Д. Муфаззалов

f = open('27-99b.txt')
n = int(f.readline())
a = [int(x) for x in f]
k, d, s_t = n // 2 + 1, n % 2, sum(a)
s = sum([a[i] * abs(i) for i in range(k - n, k)])
s_m, L, p = s, sum(a[k:]), -1
for i in range(n):
    z = a[k - n + i]
    s += 2 * (a[i] + L) - s_t - z * d
    L -= z - a[i]
    if s < s_m:
        p = i
        s_m = s
print(p + 2)