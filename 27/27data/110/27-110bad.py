with open("27-110a.txt") as F:
  N, K = map(int, F.readline().split())
  data = []
  for i in range(N):
    a, b = map( int, F.readline().split() )
    data.append( (a, b) )

def rec( pos, Lplus = 0 ):
  if pos >= N: return 0
  res0 = rec( pos+1, Lplus )
  resx = data[pos][1] + rec( pos+1, 0 )
  res = res0 if res0 > resx else resx
  if Lplus < K:
    res1 = data[pos][0] + rec(pos+1, Lplus+1)
    res = max(res, res1)
  return res

print( rec(0) )

# Если нужно увидеть, какие значения выбирались...
"""
def rec( pos, Lplus = 0, prog = '' ):
  if pos >= N: return (0, prog)
  res0, prog0 = rec( pos+1, Lplus, prog + '0' )
  resx, progx = rec( pos+1, 0, prog + 'x' )
  resx += data[pos][1]
  res, newProg = (res0, prog0) if res0 > resx else \
                 (resx, progx)
  if Lplus < K:
    res1, prog1 = rec(pos+1, Lplus+1, prog + '1')
    res1 += data[pos][0]
    if res1 > res:
      res, newProg = res1, prog1

  return res, newProg

print( *rec(0) )
"""