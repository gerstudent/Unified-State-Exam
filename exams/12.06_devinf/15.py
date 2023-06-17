def f(x, a):
    return ((x | 42 > 64) and (x | 34 <= 102)) <= (not (x | a < 70))


for a in range(1000):
    if all(f(x, a) == 1 for x in range(1000)):
        print(a)
        break
