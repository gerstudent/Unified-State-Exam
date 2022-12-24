def f(start, end):
    if start == end:
        return 1
    if start < end:
        return 0
    mn = min([x for x in map(int, str(start)) if x != 0])
    rem4 = start % 4
    res = f(start - 2, end) + f(start - mn, end)
    if rem4 != 0:
        res += f(start - rem4, end)
    return res


print(f(96, 64) * f(64, 60))
