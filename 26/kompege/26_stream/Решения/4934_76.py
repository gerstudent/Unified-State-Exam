f = open('26-76.txt')
L, N = map(int, f.readline().split())
a = [0]*(L+1)
for i in range(N):
    st, end = map(int,f.readline().split())
    a[st] += 1
    a[end] -= 1

k = 0
curr, mx, s = 0, 0, 0
for i in range(L+1):
    k+=a[i]
    if k==0:
        curr+=1
    else:
        mx = max(mx, curr)
        s += curr
        curr = 0
print(s, mx)
        
