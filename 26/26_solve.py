# 2 (1)

with open('26-97.txt') as f:
    n = int(f.readline())
    lst = []
    for i in range(n):
        d, s = map(int, f.readline().split())
        lst.append((d - 3 - 2 * s, d, s))

lst.sort(reverse=True)
pack = [lst[0]]
for i in lst:
    if i[1] <= pack[-1][0]:
        pack.append(i)

mx = 0
for i in lst:
    if i[1] <= pack[-2][0]:
        mx = max(mx, i[1])

print(len(pack), mx)

# 3 (1)

with open('26-96.txt') as f:
    n = int(f.readline())
    dict = {}
    for i in range(n):
        sh, dol = map(int, f.readline().split())
        sh = sh // 10 if sh >= 0 else -(abs(sh) // 10)
        dict[dol] = dict.get(dol, []) + [sh]

m = mx = 0
for i in sorted(dict.keys()):
    if len(dict[i]) >= m:
        m = len(dict[i])
        mx = i

print(mx, len(set(dict[mx])))

# 1 (2)

with open('26-82.txt') as f:
    n = int(f.readline())
    lst = []
    for i in range(n):
        x, y = map(int, f.readline().split())
        lst.append((x, y))

lst.sort()

maxlen = 0
maxrow = 0
prev = -1

for x, y in lst:
    if x != prev:
        st = set()
    if y % 2 != 0:
        st.add(y)
        curlen = len(st)
        if curlen > maxlen:
            maxlen = curlen
            maxrow = x
    prev = x

print(maxlen, maxrow)
