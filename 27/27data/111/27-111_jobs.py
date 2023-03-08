# Автор: Е. Джобс

fileName = '27-111a.txt'

with open(fileName) as f:
    n, X = map(int, f.readline().split())
    m = [int(x) for x in f][:n]*2
    counts = []
    for a in range(n):
        for b in range(a+1, a+n+1):
            if sum(m[a:b]) == X:
                counts += [b-a]
    print(min(counts))

with open(fileName) as f:
    n, X = map(int, f.readline().split())
    m = [int(x) for x in f][:n]*2
    counts = []
    for a in range(n):
        s = 0
        for b in range(a, a+n):
            s += m[b]
            if s == X:
                counts += [b-a+1]
            if s > X:
                break
    print(min(counts))

fileName = '27-111b.txt'

with open(fileName) as f:
    n, X = map(int, f.readline().split())
    m = [int(x) for x in f][:n]*2
    st = s = 0
    mc = float('inf')
    for i in range(2*n):
        s += m[i]
        while s > X:
            s -= m[st]
            st += 1
        if s == X:
            if mc > i - st + 1:
                mc = i - st + 1
            s -= m[st]
            st += 1

    print(mc)