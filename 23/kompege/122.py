def f(n):
    if n == cnt:
        return 1
    if n > cnt:
        return 0
    return f(n + 2) + f(n + 4) + f(n + 5)


cnt = 32
while True:
    if f(31) == 1001:
        print(cnt)
        break
    cnt += 1
