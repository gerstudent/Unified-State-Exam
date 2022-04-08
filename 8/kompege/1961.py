from itertools import product

count = 0
for i in product('ЕЛМРУ', repeat=4):
    count += 1
    lst = ''.join(i)
    if lst[0] == 'Л':
        print(count + 1)
        break
