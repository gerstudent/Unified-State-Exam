# Автор: Д. Муфаззалов

f = open('27-104b.txt')
n = int(f.readline())
k, p, i, ans = {}, {}, 2, 0
g = m = 4_043_520
while m > 1:
    while m % i == 0:
        k[i] = k.get(i, 0) + 1
        m //= i
    i += 1
for i in k:
    p[i] = [0] * (k[i] + 1)
    k[i] = [0] * k[i]
for i in range(1, n + 1):
    num = int(f.readline())
    if g % num == 0:
        for j in k:
            while num % j == 0:
                p[j].append(i)
                p[j].pop(0)
                num //= j
    else:
        for j in k:
            p[j] = [i] * len(p[j])
    z = 0
    for j in p:
        z = max(z, p[j][0])
    ans += i - z
print(ans)
f.close()
