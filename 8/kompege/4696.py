from itertools import product

cnt = 0
w = ['16', '61', '36', '63', '56', '65', '76', '67']
for x in product('01234567', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('6') == 1 and all(sub not in s for sub in w):
        cnt += 1

print(cnt)
