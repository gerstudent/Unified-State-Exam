# Автор: Д. Муфаззалов

f = open('27-106a.txt')
n = int(f.readline())
k, p, i, lmax = {}, {}, 2, 0
g = m = 8_023_320
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
    l = 0
    for j in p:
        l = max(l, p[j][0])
    if i - l > lmax:
        lmax = i - l
        index = l

print( index + 1 )
f.close()
