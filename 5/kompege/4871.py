cnt = 0
for n in range(1, 100000):
    if n % 3 == 0:
        n = n // 3
    else:
        n -= 1
    if n % 5 == 0:
        n = n // 5
    else:
        n -= 1
    if n % 11 == 0:
        n = n // 11
    else:
        n -= 1
    if n == 8:
        cnt += 1

print(cnt)
