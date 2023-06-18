f = open('26-119.txt')
N, L, M = map(int, f.readline().split())
a = []
for i in range(N):
    st, r, t = f.readline().split()
    a += [[int(st),int(st)+int(r), t]]
a.sort()

park = [0]*(L+M)
count1 = 0
count2 = 0
for i in range(N):
    st, end, t = a[i]
    if t=='A':
        for j in range(L+M):
            if park[j]<=st:
                park[j] = end
                break
        else:
            count2+=1
    if t=='B':
        for j in range(L, L+M):
            if park[j]<=st:
                park[j] = end
                count1 += 1
                break
        else:
            count2+=1
print(count1, count2)
