from itertools import permutations as pm

str = 'ТИХОРЕЦК'
glas = 'ИОЕ'
cnt = 0


def validPos(s):
    pat = 'ТИХО'
    count = 0
    for i in range(4):
        if s[i] == pat[i]:
            count += 1
    return count == 2


def valid(s):
    cntGlas = sum(s.count(c) for c in glas)
    if cntGlas != 2:
        return False
    return validPos(s)


for x in pm(str, r=4):
    s = ''.join(x)
    if valid(s):
        cnt += 1

print(cnt)
