from itertools import product, permutations as pm

w = [''.join(a) for a in product('АИОУ', repeat=2)] + [''.join(a) for a in product('БКЛН', repeat=2)]
cnt = 0
for x in pm("АБИКОЛУН", r=8):
    s = ''.join(x)
    if all(item not in s for item in w):
        cnt += 1
print(cnt)
