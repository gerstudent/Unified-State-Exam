s = '7' * 104
while '33333' in s or '777' in s:
    if '33333' in s:
        s = s.replace('33333', '7')
    else:
        s = s.replace('777', '3')

print(s)
