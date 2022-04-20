from itertools import *

no = [''.join(a) for a in product('АИОУ', repeat=2)] + [''.join(a) for a in product('БКЛН', repeat=2)]

cnt = 0
for x in permutations("АБИКОЛУН", r=8):
    s = ''.join(x)
    if all(item not in s for item in no):
        cnt += 1
print(cnt)
