# Автор: Е. Джобс

with open('27-115b.txt') as f:
    n = int(f.readline())
    m = [f.readline() for _ in range(n)]
m.sort()
a = [set(), set()]
for i in range(n):
    a[i%2].add(m[i])
print((1 + len(a[0]) + len(a[1])) // 2)


with open('27-115b.txt') as f:
    n = int(f.readline())
    m = [f.readline() for _ in range(n)]
m.sort()
print( (1 + len(set(m[::2])) + len(set(m[1::2]))) // 2 )
