from itertools import product

cnt = 0
for x in product('ОГЭИНФ', repeat=6):
    s = ''.join(x)
    if (s[0] == 'Э' or s[0] == 'О') and s.endswith('НФ') and s.count('ИГ') >= 1 and s.count('ОГЭ') == 0:
        cnt += 1

print(cnt)
