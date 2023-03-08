with open("27-110b.txt") as F:
  N, K = map(int, F.readline().split())
  data = []
  for i in range(N):
    a, b = map( int, F.readline().split() )
    data.append( (a, b) )

A = [ [0]*(K+1) for i in range(N+1) ]
for pos in range(N):
  a, b = data[pos]
  for k in range(K+1):
    if k == 0:
      R = max( A[pos][0], # если пропустить пару
               b + max(A[pos][j] for j in range(K+1)) ) # выбрать отрицательное
    else:
      R = max( A[pos][k], # если пропустить пару
               A[pos][k-1]+a ) # выбрать положительное
    A[pos+1][k] = R

print( max( A[N][k] for k in range(K+1) ) )