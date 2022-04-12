from itertools import product

count = 0
for i in product('01234', repeat=6):
    lst = ''.join(i)
    if lst[0] not in '01' and lst[-1] not in '34':
        count += 1
print(count)

# Решение в одну строку: print(len([i for i in range(int('200000', 5), int('444442', 5) + 1) if str(i % 5) not in '34']))
