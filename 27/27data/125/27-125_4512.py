# Автор: 4512

f = open('27-125b.txt')
n = int(f.readline())
a = [int(f.readline()) for _ in range(n)]
s = sum(a)
best_s = sum(a) // 2 + (sum(a) % 2)
st = k = 0
mn_delta = mn_r = float('inf')

for i in range(n*2):
    k += a[i%n]
    while k - a[st%n] >= best_s:
        k -= a[st%n]
        st += 1
    if abs(s - 2 * k) < mn_delta:
        mn_delta = abs(s - 2 * k)
        mn_r = min(abs(i - st), n - abs(i - st) - 2)
    elif abs(s - 2 * k) == mn_delta:
        mn_r = min(mn_r, abs(i - st), n - abs(i - st) - 2)
print( mn_r )