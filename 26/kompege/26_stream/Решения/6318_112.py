f = open('26-112.txt')
N, M = map(int, f.readline().split())
a = []
for i in range(M):
    st, r = map(int,f.readline().split())
    a.append([st, st+r, r])
a.sort(key = lambda x: x[0])

bank = [0]*N
bank_count = [0]*N
last = 0
for i in range(M):
    st, end, r = a[i]
    for j in range(N):
        if bank[j]<=st:
            bank[j] = end
            bank_count[j]+=1
            last = st
            break
    else:
        j = bank.index(min(bank))
        if bank[j]<=1440:
            last = bank[j]
            bank[j] =bank[j] + r
            bank_count[j]+=1
print(max(bank_count), last)
        
    
