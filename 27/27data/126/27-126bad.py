# Решение на 1 балл
# Автор: К. Багдасарян

with open('27-126a.txt') as f:
    n = int(f.readline())
    d = [0] * n
    for i in range(n):
        a,b = f.readline().split()
        d[i] = int(b)

mx = 0
for i in range(n):
    for j in range(i+1,n):
        if d[j] > d[i]:
            mx = max(j - i, mx)
            break
print(mx)
