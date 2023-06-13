d = {}
with open('27B_9444.txt') as f:
    n = int(f.readline())
    for i in range(n):
        x = int(f.readline())
        if x % 7 not in d.keys():
            d[x % 7] = []
        else:
            d[x % 7].append(x)

mx0 = max(i for i in d[0] if i % 49 != 0)
mx = 0
for i in d.values():
    for j in i:
        if j % 7 != 0:
            mx = max(mx, j)

print(mx0 * mx)
