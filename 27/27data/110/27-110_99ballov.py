# Автор: 99 баллов

file = open("27.txt")
n, k = map(int, file.readline().split())
a = []
b = []
for i in range(n):
    a_i, b_i = map(int, file.readline().split())
    a.append(a_i)
    b.append(b_i)
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]
dp = [[-10 ** 9 for i in range(n + 1)] for i in range(k + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(k + 1):
        dp[j][i] = dp[j][i - 1]
        if j == 0:
            for p in range(k + 1):
                dp[0][i] = max(dp[0][i], dp[p][i - 1] + b[i - 1])
        else:
            for p in range(1, j + 1):
                if p <= i:
                    dp[j][i] = max(dp[j][i], dp[j - p][i - p] + prefix[i] - prefix[i - p])
res = 0
for i in range(n + 1):
    for j in range(k + 1):
        res = max(res, dp[j][i])
print(res)