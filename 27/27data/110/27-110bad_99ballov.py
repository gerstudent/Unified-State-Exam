file = open("27.txt")
n, k = map(int, file.readline().split())
a = []
b = []
for i in range(n):
    a_i, b_i = map(int, file.readline().split())
    a.append(a_i)
    b.append(b_i)

def dp(i, n, s, cur, k):
    global a, b
    if i == n:
        return s
    if cur == k:
        return max( dp(i + 1, n, s, cur, k),
                    dp(i + 1, n, s + b[i], 0, k))
    else:
        return max( dp(i + 1, n, s + a[i], cur + 1, k),
                    dp(i + 1, n, s, cur, k),
                    dp(i + 1, n, s + b[i], 0, k))

print(dp(0, n, 0, 0, k))

