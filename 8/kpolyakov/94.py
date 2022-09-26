from itertools import permutations as pm

count = 0
for x in pm("ПАНЕЛЬ", r=6):
    s = ''.join(x)
    if s[0] != 'Ь' and "ЕЬ" not in s:
        count += 1

print(count)
