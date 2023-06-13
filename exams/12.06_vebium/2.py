from itertools import product

for x, y, z in product((0, 1), repeat=3):
    f = (y <= x) and (x <= z)
    if f:
        print(y, z, x)
