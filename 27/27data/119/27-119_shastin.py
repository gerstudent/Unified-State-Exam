f = open('27-119b.txt')
n, k =  map(int, f.readline().split())
center = k//2
count = 0
buf = []
 
 
total = 0
for _ in range(k):
     x = int(f.readline())
     if x==0: count += 1
     buf.append(x)
 
 
a = sum(buf[:center])
b = sum(buf[center+1:])
if a==b and count>=1: total += 1
 
for _ in range(n-k):
     x = int(f.readline())
     a += buf[center]
     b -= buf[center+1]
     m = buf.pop(0)
     a-= m
     if m==0: count -= 1
     buf.append(x)
     if x==0: count += 1
     b += x
     if a==b and count>=1: total += 1
 

print(total)
