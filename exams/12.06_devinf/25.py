from fnmatch import fnmatch


def prime(n):
    ans = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        ans.append(n)
    return sorted(ans)


for x in range(0, 10 ** 4):
    if fnmatch(str(x), '*2?2'):
        res = prime(x)
        if len(res) == 7:
            print(x, max(res))
