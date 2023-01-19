from fnmatch import fnmatch

for x in range(700000, 750000):
    c1 = fnmatch(str(x), '*0??3*')
    c2 = fnmatch(str(x), '*4??2')
    c3 = fnmatch(str(x), '*1*')
    if c1 + c2 + c3 == 0 and x % 13 == 0:
        print(x, sum(map(int, str(x))))
