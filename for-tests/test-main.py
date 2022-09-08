from itertools import *

word = 'ГЕПАРД'
cnt = 0
for x in product(word, repeat=5):
    s = ''.join(x)
    if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
        cnt += 1
print(cnt)
