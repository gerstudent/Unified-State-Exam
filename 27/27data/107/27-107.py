# Автор: 99 баллов

file = open("27-107b.txt")
n = int(file.readline())
arr = []
used = [-1] * n
maxTime = 0
for i in range(n):
    s, f = map(int, file.readline().split())
    arr.append((s, -i))
    arr.append((f, i))
    maxTime = max(maxTime, s, f)
arr.sort()
dp = [0] * (maxTime + 1)
cur = 0
for i in range(1, maxTime + 1):
    dp[i] = dp[i - 1]
    while cur < len(arr) and arr[cur][0] == i:
        if arr[cur][1] >= 0 and used[arr[cur][1]] > -1:
            dp[i] = max(dp[i], used[arr[cur][1]] + 1)
        else:
            used[arr[cur][1] * -1] = dp[i]
        cur += 1
print(dp[maxTime])


