f = open("27-101a.txt", "w")
n = 1000
from random import randint
print( n, file=f)
for i in range(n):
  print( randint(10,1000), file=f)

f.close()