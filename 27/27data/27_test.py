def dtb(x, y):
    w = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''

    while x > 0:
        if x % y > 9:
            s += w[x % y - 10]
        else:
            s += str(x % y)
        x //= y
    return s[::-1]
