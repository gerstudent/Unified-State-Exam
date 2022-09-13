from itertools import product

cnt = 0
cnt1 = 0
cnt2 = 0
for x in product('АОУ', repeat=5):
    cnt += 1
    s = ''.join(x)
    if s == 'УАУАУ':
        cnt2 = cnt
    if s == 'ОУОУА':
        cnt1 = cnt
print(cnt2 - cnt1 + 1)
