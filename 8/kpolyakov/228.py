from itertools import permutations as pm

cnt = 0
word = 'МАРИНА'
for x in set(pm(word)):
    s = ''.join(x)
    if s[0] in 'МРН':
        cnt += 1

print(cnt)
