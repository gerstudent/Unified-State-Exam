# Автор: Д. Муфаззалов

f = open('27-101b.txt')
n = int(f.readline())
m = 858967

k, i, d, ans = {}, 2, {}, 0
while m > 1:
    while m % i == 0:
        k[i] = k.get(i, 0) + 1
        m //= i
    i += 1

for i in k:
    d[i] = [0] * k[i]

for i in range(1, n + 1):
    num = int(f.readline())
    for j in d:
        while num % j == 0:
            d[j].pop(0)
            d[j].append(i)
            num //= j
    ans += i-min(min(d.values()))

print(ans)
