# Автор: Е. Джобс

with open('27-105b.txt') as f:
    n, k = map(int, f.readline().split())
    m = [int(f.readline()) for i in range(n)]
    sum_m = 2*sum(m)
    ps = [sum(m[i]*min(i, n-i)**2 for i in range(n)),
          sum(m[i]*min(abs(i-1), n-abs(i-1))**2 for i in range(n))]
    #print( 1, ps[0]*k*k )
    #print( 2, ps[1]*k*k )
    ms = min(ps)
    mi = ps.index(ms)
    rs = ps[1] - ps[0]
    s = ps[1]
    for i in range(2, n):
        mid = i + n//2 - 1
        if n % 2 == 0:
          rs += sum_m - 2*n*m[mid % n]
        else:
          rs += sum_m - n*(m[mid % n] + m[(mid + 1) % n])
        s += rs
        if s < ms:
            ms = s
            mi = i
        #print( i+1, s*k*k )
    print( 'Ответ:', mi+1, ms*k*k)

