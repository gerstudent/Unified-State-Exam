f = open('26-75.txt')
N = int(f.readline())
a = [0]*1_000_000
for i in range(N):
    st, end = map(int, f.readline().split())
    a[st]+=1
    a[end]-=1

k = 0
minutes = 0
max_pas = 0
for i in range(1_000_000):
    k+=a[i]
    if k>0:
        minutes+=1
    max_pas = max(max_pas, k)
print(max_pas, minutes)
    
        
