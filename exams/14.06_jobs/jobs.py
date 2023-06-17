# from itertools import product
#
# for x, y, z, w in product((0, 1), repeat=4):
#     f = (x <= y) and (not y == z) and w
#     if f:
#         print(z, w, y, x)


# for n in range(1000):
#     b = bin(n)[2:]
#     tmp = b
#     if n % 2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#     if tmp.count('1') % 2 != 0:
#         b = b + '1'
#     else:
#         b = b + '0'
#
#     r = int(b, 2)
#     if r > 2023:
#         print(r)
#         break


# from turtle import *
#
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(9):
#     fd(15 * r)
#     rt(90)
#     fd(25 * r)
#     rt(90)
#
# up()
# bk(10 * r)
# rt(90)
# down()
# for i in range(8):
#     fd(15 * r)
#     lt(90)
#     fd(25 * r)
#     lt(90)
#
# up()
# fd(6 * r)
# lt(90)
# down()
# for i in range(7):
#     fd(15 * r)
#     rt(90)
#     fd(25 * r)
#     rt(90)
#
# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x * r, y * r)
#         dot(3, 'blue')
#
# update()
# exitonclick()


# from itertools import product
#
#
# for i in product('0123456789abcde', repeat=5):
#     s = ''.join(i)

# n = 19 * 262_144
# print(n // 1024)

# for n in range(101, 1000):
#     s = '5' * n
#     while '555' in s or '11' in s or '2' in s:
#         if '555' in s:
#             s = s.replace('555', '1', 1)
#         if '11' in s:
#             s = s.replace('11', '25', 1)
#         if '2' in s:
#             s = s.replace('2', '5', 1)
#     if s == '15':
#         print(n)
#         break


# al = '0123456789abc'
# for x in al:
#     a = int(f'537{x}623', 13) - int(f'6{x}35{x}2', 13)
#     if a % 3 == 0:
#         print(x, a)


# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return (d(x, 10) and d(x, 26) and (x >= 300)) <= (a <= x)
#
#
# for a in range(0, 10 ** 3):
#     if all(f(x, a) == 1 for x in range(10 ** 4)):
#         print(a)


# def f(n):
#     if n >= 2222:
#         return n
#     else:
#         return f(n + 5) + 7
#
#
# print(f(45) - f(49))


# with open('17_9547.txt') as f:
#     data = [int(x) for x in f.readlines()]
#
# mn = min(i for i in data if len(str(i)) == 3 and str(i)[1] == '1' and str(i)[2] == '1')
# ans = []
# for i in range(len(data) - 1):
#     x, y = data[i], data[i + 1]
#     c1 = len(str(x)) != 3 ^ len(str(y)) != 3
#     c2 = abs(x - y) % mn == 0
#     if c1 and c2:
#         ans.append(x + y)
#
# print(len(ans), max(ans))


# from functools import lru_cache
#
#
# def moves(h):
#     return h + 2, h + 4, h * 3
#
#
# @lru_cache(None)
# def g(h):
#     if h >= 82:
#         return 'w'
#     if any(g(x) == 'w' for x in moves(h)):
#         return 'p1'
#     if all(g(x) == 'p1' for x in moves(h)):
#         return 'v1'
#     if any(g(x) == 'v1' for x in moves(h)):
#         return 'p2'
#     if all(g(x) == 'p1' or g(x) == 'p2' for x in moves(h)):
#         return 'v2'
#
#
# ans19, ans20, ans21 = [], [], []
# for s in range(1, 82):
#     # if g(s) == 'v1':
#     #     ans19.append((s, g(s)))
#
#     if g(s) == 'v2':
#         ans21.append((s, g(s)))
#
# print(ans21)


# d = {"0": 0}
# data = []
# with open('22.txt') as f:
#     for s in f:
#         data.append(s.replace(';', ' ').split())
#
# while len(d) != len(data) + 1:
#     for s in data:
#         idB, time, idA = s[0], s[1], s[2:]
#         if all(sub in d for sub in idA):
#             d[idB] = int(time) + max(d[sub] for sub in idA)
#
# print(max(d.values()))


# def f(n, k):
#     if n > k:
#         return 0
#     if n == k:
#         return 1
#     return f(n + 3, k) + f(n * 2, k)
#
#
# print(f(3, 30) * f(30, 105))


# with open('24_9552.txt') as f:
#     s = f.readline()
#
# ln = 1
# i = 0
# res = ''
# ans = []
# s = s.replace('PC', '1').replace('CSGO', '2')
# while i != len(s):
#     if s[i] in '12':
#         res += s[i]
#     else:
#         ans.append(res)
#         res = ''
#     i += 1
#
# mx = max(ans, key=len)
# c = 0
# for i in mx:
#     if i == '1':
#         c += 2
#     else:
#         c += 4
#
# print(c)


# from fnmatch import fnmatch
#
# for x in range(0, 10 ** 9, 13):
#     if fnmatch(str(x), '24*68?35'):
#         print(x, x // 13)


# with open('27_test.txt') as f:
#     n, k = map(int, f.readline().split())
#     cnt = s = 0
#     w = 111
#     pref = [0] * w
#
#     for i in range(n):
#         x = int(f.readline())
#         s += x
#
#         if s % w == 0:
#             cnt += 1
#
#         cnt += pref[s % w]
#         pref[s % w] += 1
#
# print(cnt, end=' ')








