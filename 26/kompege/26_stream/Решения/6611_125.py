f = open('26-125.txt')
N, P = map(int,f.readline().split())
a = []
for i in range(N):
    st, mana = map(int,f.readline().split())
    if mana>1:
        a.append([st, mana//2])
a.sort()

kotl = [0]*P
count = 0
mx = 0
for i in range(len(a)):
    st, zel = a[i]
    for j in range(P):
        if kotl[j]<=st:
            kotl[j] = st+zel if kotl[j]==0 else st+zel+2
            count += zel if kotl[j]<=1440 else 1440 - st - 2
            mx = max(mx, zel if kotl[j]<=1440 else 1440 - st - 2)
            break
print(count, mx)
