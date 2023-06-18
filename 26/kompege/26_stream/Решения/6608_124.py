f = open('26-124.txt')
K, M, N = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort(reverse=1)
rows = [M]*K
count = 0
for i in range(N):
    places = a[i]
    for j in range(K):
        if rows[j]>=places:
            rows[j]-=places
            count += 1
            break
print(count, sum(rows))
        
