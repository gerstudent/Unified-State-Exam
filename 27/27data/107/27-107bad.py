F = open("27-107a.txt")
N = int(F.readline())

data = []
for i in range(N):
   s = F.readline().split()
   data.append( tuple(map(int,s)) )
F.close()

data.sort()
print( data )

def intersect( used, newItem ):
   for u in used:
     if u[0] <= newItem[0] <= u[1] or u[0] <= newItem[1] <= u[1] or \
        newItem[0] <= u[0] <= newItem[1] or \
        newItem[0] <= u[1] <= newItem[1]:
        return True
   return False

maxLen = 0
def rec( used, remains ):
  global maxLen
  if len(used) > maxLen:
    maxLen = len(used)
    print( maxLen, used )
  for i, r in enumerate(remains):
    if not intersect(used, r):
       rec( used+[r], remains[i+1:] )

rec( [], data )

print( maxLen )


