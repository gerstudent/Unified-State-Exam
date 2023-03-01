with open('17-316.txt') as f:
    data = [int(i) for i in f.readlines()]

mx1 = max(data)
res = set(data)
res.remove(mx1)
mx2 = max(res)


def isGood(x, y):
    arithm = (x + y) / 2
    geom = (x * y) ** 0.5
    sa = str(arithm).split('.')
    sg = str(geom).split('.')
    c1 = int(sa[0]) != 0 and int(sa[1]) == 0
    c2 = int(sg[0]) != 0 and int(sg[1]) == 0
    if c1 and c2:
        return True
    return False


cnt = 0
mini = 10 ** 6
for i in range(0, len(data) - 2):
    x, y, z = data[i], data[i + 1], data[i + 2]
    if isGood(x, y) or isGood(y, z) or isGood(x, z):
        if x + y + z < mx1 + mx2:
            cnt += 1
            mini = min(x + y + z, mini)

print(cnt, mini)
