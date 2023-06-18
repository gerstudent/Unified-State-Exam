f= open('26-122.txt')
K, N = map(int,f.readline().split())
a = []
for i in range(N):
    st, end = map(int,f.readline().split())
    a.append([st, end])
a.sort()

house = [0]*N
last = 0
for i in range(N):
    st, end = a[i]
    for j in range(N):
        if house[j]<st:
            house[j] = end
            last = st
            break
house = [x for x in house if x!=0]
print(len(house)/K, len([x for x in house if x>last]))
