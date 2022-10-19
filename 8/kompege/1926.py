from itertools import *

cnt = 0
word = '012345'
for x in product(word, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        f = True
        for j in range(len(s) - 1):
            prev = int(s[j])
            nxt = int(s[j + 1])
            if ((prev % 2 == 0 and nxt % 2 == 0) or (prev % 2 != 0 and nxt % 2 != 0)) == 1:
                f = False
                break
        if f:
            cnt += 1
print(cnt)
