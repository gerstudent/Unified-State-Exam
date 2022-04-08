from itertools import permutations

count = 0
for i in permutations('ДЕЙКСТРА', r=6):
    lst = ''.join(i)
    if any(item in lst for item in ['ЙД', 'ЙС', 'ЙР', 'ЙК', 'ЙТ']):
        count += 1

print(count)
