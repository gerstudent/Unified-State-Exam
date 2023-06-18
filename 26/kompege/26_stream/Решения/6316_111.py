f = open('26-111.txt')
K = int(f.readline())
N = int(f.readline())
a = []
for i in range(N):
    st, end = map(int, f.readline().split())
    a += [[st,end]]
a.sort()
k = [0]*(K+1)

count = 0
last = 0

for i in range(N):
    st, end = a[i]
    for j in range(1, K+1):
        if k[j]<st:
            k[j] = end
            count += 1
            last = j
            break
print(count, last)
