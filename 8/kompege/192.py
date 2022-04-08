from itertools import product

count = 0
for i in product('АБВГДЯ', repeat=5):
    lst = ''.join(i)
    if lst.count('Я') == 3:
        count += 1

print(count)
