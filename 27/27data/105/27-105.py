with open("27-105b.txt") as F:
  N, R = map(int, F.readline().split())
  data = [ float(F.readline()) for i in range(N) ]

sum2x = 2*sum(data)
energy0 = sum( data[i]*min(i,N-i)**2 for i in range(N) )
energy1 = sum( data[i]*min(abs(i-1),N-abs(i-1))**2 for i in range(N) )
if energy0 < energy1:
  bestPos, minEnergy = 0, energy0
else:
  bestPos, minEnergy = 1, energy1

#print( 1, energy0*R*R )
#print( 2, energy1*R*R )

diff = energy1 - energy0
energy = energy1
for i in range(2, N):
  mid = i + N//2 - 1  # номер самого дальнего датчика (или одного из)
  if N % 2 == 0: # единственный самый дальний датчик
    diff += sum2x - 2*N*data[mid % N]
  else: # два самых дальних датчика
    diff += sum2x - N*data[mid % N] - N*data[(mid+1) % N]
  energy += diff
  if energy < minEnergy:
    bestPos, minEnergy = i, energy
  #print( i, energy*R*R )

print( bestPos+1, minEnergy*R*R )
