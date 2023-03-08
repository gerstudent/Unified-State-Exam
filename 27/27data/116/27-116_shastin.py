# Автор: Л. Шастин

F = open('27-116a.txt')
N, K, D = map(int, F.readline().split())
A = [int(x) for x in F]
sA = sum(A)
k = [[0]*D for j in range(K)]
s, count = 0, 0
for i in range(N):
    s += A[i]
    if s%K == 0 and (sA - s)%D == 0:
        count += 1
    count += k[s%K][(D - (sA - s)%D)%D]
    k[s%K][s%D] += 1
print(count)
F.close()