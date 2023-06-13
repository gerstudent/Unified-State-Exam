def f(n, k):
    if n > k or n == 35:
        return 0
    if n == k:
        return 1
    dig = n // (10 ** (len(str(n)) - 1))
    if dig == 9:
        return f(n + 5, k)
    else:
        return f(n + 5, k) + f(n + (10 ** (len(str(n)) - 1)), k)


print(f(30, 60))
