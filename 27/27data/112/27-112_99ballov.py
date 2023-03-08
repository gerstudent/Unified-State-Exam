file = open("27-112a.txt")
n, k = map(int, file.readline().split())

used = [0] * (10 ** 6 + 1)
for i in range(n):
    used[int(file.readline())] += 1

res = 0
for i in range(1, 10 ** 6 + 1):
    cnt = 0
    for j in range(i, 10 ** 6 + 1, i):
        cnt += used[j]
    if cnt >= k:
        res = i
print(res)
