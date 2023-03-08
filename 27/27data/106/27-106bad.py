# Автор: Д. Муфаззалов

f = open('27-106a.txt')
n = int(f.readline())
a, m = list(map(int, f.readlines())), 8_023_320

for i in range(1, n + 1):
    p = 1
    for h in a[:i]:
        p *= h
    if m % p == 0:
        ans, index = i, 0
    else:
        for j in range(i, n):
            p //= a[j - i]
            p *= a[j]
            if m % p == 0:
                ans, index = i, j - i + 1
                break

print( index + 1 )