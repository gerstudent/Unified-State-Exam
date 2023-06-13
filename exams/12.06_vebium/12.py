s = 21 * '3' + 22 * '4' + 23 * '5'
s1, s2, s3 = '333', '4444', '55555'
while s1 in s or s2 in s or s3 in s:
    if s1 in s:
        s = s.replace(s1, '44', 1)
    else:
        if s2 in s:
            s = s.replace(s2, '555', 1)
        elif s3 in s:
            s = s.replace(s3, '3', 1)

print(sum(map(int, s)))
