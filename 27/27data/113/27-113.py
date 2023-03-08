F = open("27-113b.txt")
N = int( F.readline() )

tariff = { 1: 15, 11: 40, 21: 70 }

def reduce( data ):
  data = sorted(data)
  i = 0
  while i < len(data)-1:
    pos1, pay1 = data[i]
    pos2, pay2 = data[i+1]
    if pos1 < pos2 and pay2 <= pay1:
      del data[i]
      i -= 1
    elif pos1 == pos2: # после сортировки pay2 >= pay1
      del data[i+1]
      i -= 1
    i += 1
  return data

pos = int( F.readline() )  # читаем первое число отдельно
passFor = [ (pos+count-1, money)
            for count, money in tariff.items() ]
for i in range(N-1):
  pos = int( F.readline() )
  #print( '*', pos )
  k = 0
  while k < len(passFor):
    posPaid, sumMoney= passFor[k]
    if pos > posPaid:
       passFor.pop(k)
       k -= 1
       for count, money in tariff.items():
          passFor += [ (pos+count-1, sumMoney+money) ]
    k += 1
  passFor = reduce( passFor )
  #print( passFor )

paidFor, minSum = min( passFor, key = lambda x: x[1] )
print( minSum )

F.close()

"""
# Если нужно определить, для каких номеров платить...

pos = int( F.readline() )  # читаем первое число отдельно
passFor = [ (pos+count-1, money, [pos])
            for count, money in tariff.items() ]
for i in range(N-1):
  pos = int( F.readline() )
  #print( '*', pos )
  k = 0
  while k < len(passFor):
    posPaid, sumMoney, way = passFor[k]
    if pos > posPaid:
       passFor.pop(k)
       k -= 1
       for count, money in tariff.items():
          passFor += [ (pos+count-1, sumMoney+money, way+[pos]) ]
    k += 1
  passFor = reduce( passFor )
  #print( passFor )

paidFor, minSum, bestWay = min( passFor, key = lambda x: x[1] )
print( minSum )
print( bestWay )
"""
