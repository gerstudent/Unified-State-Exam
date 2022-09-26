from itertools import product

cnt = 0


def valid(word):
    pat = 'ВОЛК'
    count = 0
    for i in range(len(pat)):
        if word[i] == pat[i]:
            count += 1
    return count == 2


for x in product('ПОЛЯКВ', repeat=4):
    s = ''.join(x)
    if valid(s):
        cnt += 1

print(cnt)
