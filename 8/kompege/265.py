from itertools import product

count = 0
for i in product("АГИЛМОРТ", repeat=4):
    count += 1
    lst = ''.join(i)
    if lst[2] == 'И' and lst[3] == 'М':
        print(count)  # Answer - last number
