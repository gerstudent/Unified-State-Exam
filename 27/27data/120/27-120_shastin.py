# Автор: Л. Шастин

F = open('27-120b.txt')
N = int(F.readline())
count, l = 0, 0
buf = []
for i in range(2):
    buf += [int(F.readline())]
    count += i + 1
for i in range(2, N):
    x = int(F.readline())
    if x == 1 and buf[-1] == 1 and buf[-2] == 1:
        l = i - 1
    count += i + 1 - l
    buf.pop(0)
    buf += [x]
print(count)
F.close()

F = open('27-120a.txt')
N = int(F.readline())
A = [int(x) for x in F]
k = [0]*N
for i in range(N - 2):
    if A[i] == 1 and A[i+1] == 1 and A[i+2] == 1:
        k[i+1] = 1
count, l = 0, 0
for i in range(N):
    count += (i + 1 - l)
    if k[i] == 1:
        l = i
print(count)
F.close()

count = 0
for i in range(N):
    t = []
    for j in range(i, N):
        t += [A[j]]
        if len(t) < 3:
            count += 1
        else:
            if all(((t[i] == 1) + (t[i+1] == 1) + (t[i+2] == 1)) != 3 for i in range(len(t) - 2)):
                count += 1
print(count)


F = open('27-120b.txt')
N = int(F.readline())
count, l = 0, 0
p = [0] + [0]*N
for i in range(1, N + 1):
    p[i] = p[i-1] + int(F.readline())
    if i - 3 > 0 and p[i] - p[i-3] == 3:
        l = i - 2
    count += (i - l)
print(count)
F.close()


F = open('27-120b.txt')
N = int(F.readline())
A = [int(x) for x in F]
s = '*'
for x in A:
     s += str(x) + '*'
while '*1*1*1*' in s:
     s = s.replace('*1*1*1*', '*1*1* *1*1*')
count = 0
for x in s.split():
     m = len([int(m) for m in x.split('*') if m!=''])
     count += m*(m+1)//2 - 1
print(count + 1)
F.close()







