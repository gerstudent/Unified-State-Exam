f = open('26-66.txt')
N, K = map(int, f.readline().split())

START = K
END = K + 24*60*60*1000

a = [ 0 ] * (24*60*60*1000 + 1)
for i in range(N):
    st, end = map(int, f.readline().split())
    if st < START: st = START
    if end == 0 or end > END: end = END
    if st <= END and end >= START:
        a[st-K]+=1
        a[end-K]-=1
        

k = 0
m, ml = 10**20, 0
for i in range(24*60*60*1000):
    k+=a[i]
    if k<m:
        m, ml = k, 0
    if m==k: ml += 1
print(m, ml)
    
