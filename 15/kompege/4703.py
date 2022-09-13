def f(x, a):
    return ((x % 2 == 0) <= (not (x % 3 == 0))) or (x + a >= 100)


for a in range(0, 100):
    cnt = 0
    for x in range(0, 1000):
        if f(x, a):
            cnt += 1
    if cnt == 999:
        print(a)
        break
