with open('112/27-112a.txt') as f:
    n, k = map(int, f.readline().split())
    used = [0] * (10 ** 6 + 1)
    for i in range(n):
        used[int(f.readline())] += 1

ans = 0
for i in range(1, 10 ** 6 + 1):
    c = 0
    for j in range(i, 10 ** 6 + 1, i):
        c += used[j]
    if c >= k:
        ans = i

print(ans)
