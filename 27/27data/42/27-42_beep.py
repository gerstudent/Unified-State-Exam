# Автор: beep

Fin = open("27-42.txt")

N = int(Fin.readline())
s1 = s2 = s3 = 0
swap = [[], []]
diff = [ 1e10, 1e10 ]
flag = 0

for i in range(N):
   a, b, c = map( int, Fin.readline().split() )
   a, b, c = sorted( [a, b, c] )
   s1 += a
   s2 += b
   s3 += c
   if b % 2 != a % 2:
     swap[c % 2].append(c - (a if a % 2 != c % 2 else b))
   elif b % 2 != c % 2:
     flag += b
     delta = c - b
     if delta < diff[0]:
       diff = [ delta, diff[0] ]
     elif c - b < diff[1]:
       diff[1] = delta

Fin.close()

for a in swap:
   a.sort()

if s1 % 2 == 0  and  s2 % 2 == 0:
   print( s3 )
elif s1 % 2 != 0 and s2 % 2 != 0:
   if swap[0] or swap[1]:
     print( s3 )
   else:
     print(s3 - sum(diff))
else:
     delta = [diff[0]]
     if flag % 2: swap[0], swap[1] = swap[1], swap[0]
     if swap[0]: delta.append(swap[0][0])
     if swap[1] and (swap[0] or len(swap[1]) > 1): delta.append(swap[1][0])
     print(s3 - min(delta))