def divs(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return 0, 1


cnt = 0
for i in range(800000, 900000):
    ds = divs(i)
    if sum(ds) % 138 == 0:
        print(i, sum(ds))
        cnt += 1
        if cnt == 5:
            break
