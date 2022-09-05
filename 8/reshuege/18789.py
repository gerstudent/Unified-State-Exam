from itertools import product

count = 0
for i in product('ЕНОС', repeat=4):
    count += 1
    lst = ''.join(i)
    if lst == 'СЕЕЕ':
        print(count)
        break
