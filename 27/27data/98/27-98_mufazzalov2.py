# Автор: Д. Муфаззалов

f = open('27-98b.txt')
n, k = list(map(int, f.readline().split()))
a, L, j = [-n] * k, n, 0
for i in range(n):
    num = int(f.readline()) - 1
    a[num] = i
    if num == j: j = a.index(min(a))
    L = min(L, i - a[j])
print(L + 1)
