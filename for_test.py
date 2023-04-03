with open('26_1257.txt') as f:
    n = int(f.readline())
    data = [int(i) for i in f.readlines()]
    st = set(data)

ans = []
for i in range(n):
    for j in range(i + 1, n):
        sm = data[i] + data[j]
        c1 = sm % 2 != 0
        c2 = sm in st
        if c1 and c2:
            ans.append(sm)

print(len(ans), max(ans))
