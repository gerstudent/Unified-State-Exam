# Автор: Д. Муфаззалов

f = open('27-104a.txt')
n = int(f.readline())
m = 4043520
a = list(map(int, f.readlines()))
ans = 0
for i in range(1, n + 1):
    p = 1
    for h in a[:i]:
        p *= h
    if m % p == 0: ans += 1
    for j in range(i, n):
        p //= a[j - i]
        p *= a[j]
        if m % p == 0: ans += 1
print(ans)
