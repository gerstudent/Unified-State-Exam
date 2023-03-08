# Автор: Д. Муфаззалов

f = open('27-98b.txt')
n, k = list(map(int, f.readline().split()))
a, L = [-n] * k, n
for i in range(n):
    a[int(f.readline()) - 1] = i
    L = min(L, i - min(a))
print(L + 1)
