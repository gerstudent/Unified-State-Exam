# Автор: Е. Джобс

with open('27-125b.txt') as f:
    n = int(f.readline())
    m = [int(f.readline()) for _ in range(n)]

mn_w = sum(m) // 2 + sum(m) % 2
c = 0
mn = mn_r = float('inf')
s = st = 0
for i in range(n):
    while s < mn_w:
        s += m[st % n]
        if mn > abs(mn_w - s):
            mn = abs(mn_w - s)
            mn_r = min(st - i, n - (st-i) - 2)
        elif mn == abs(mn_w - s):
            mn_r = min(mn_r, st - i, n - (st-i) - 2)
        st += 1
    s -= m[i]
    if mn > abs(mn_w - s):
        mn = abs(mn_w - s)
        mn_r = min((st-1) - (i+1), n - ((st-1)-(i+1)) - 2)
    elif mn == abs(mn_w - s):
        mn_r = min(mn_r, (st-1) - (i+1), n - ((st-1)-(i+1)) -2)
print(mn_r)
