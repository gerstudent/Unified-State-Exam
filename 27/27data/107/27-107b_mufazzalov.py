# Автор: Д. Муфаззалов

f = open('27-107b.txt')
n, a = int(f.readline()), []
for i in range(n):
    a.append(list(map(int, f.readline().split())))

a.sort( key=lambda x: x[1] )

ans, b = 1, a[0][1]
for i in a:
    if b < i[0]:
        b = i[1]
        ans += 1
print(ans)
