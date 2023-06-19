with open('26-76.txt') as f:
    l, n = map(int, f.readline().split())
    day = [0] * (l + 1)
    for i in range(n):
        start, end = map(int, f.readline().split())
        day[start] += 1
        day[end] -= 1

ln = 0
cnt = 0
mx = 0
sm = 0
for i in range(l + 1):
    cnt += day[i]
    if cnt == 0:
        ln += 1
    else:
        mx = max(mx, ln)
        sm += ln
        ln = 0

print(sm, mx)
