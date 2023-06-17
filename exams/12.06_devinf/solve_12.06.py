# from math import sqrt
#
#
# def moves(h):
#     x, y = h
#     return (x * 2, y), (x, y + 3), (x, y + 4)
#
#
# def g(h):
#     if sqrt(h[0] ** 2 + h[1] ** 2) >= 14:
#         return 'w'
#     if any(g(p) == 'w' for p in moves(h)):
#         return 'p1'
#     if all(g(p) == 'p1' for p in moves(h)):
#         return 'v1'
#     if any(g(p) == 'v1' for p in moves(h)):
#         return 'p2'
#     if all(g(p) == 'p1' or g(p) == 'p2' for p in moves(h)):
#         return 'v2'
#
#
# ans19, ans20, ans21 = [], [], []
# for s in range(1, 14):
#     res = g((3, s))
#     if res is not None:
#         if res == 'v1':
#             ans19.append((s, res))
#         if res == 'p2':
#             ans20.append((s, res))
#         if res == 'v2':
#             ans21.append((s, res))
#
# print(min(ans19), sorted(ans20), ans21, sep='\n')


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
#     if n > k or n == 13:
#         return 0
#     if n == k:
#         return 1
#     return f(n + 1, k) + f(n * 2, k) + f(n * 3, k)
#
#
# print(f(3, 8) * f(8, 18))


# with open('24.txt') as f:
#     s = f.readline()
#
# cnt, mx = 1, 0
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         cnt += 1
#     else:
#         mx = max(mx, cnt)
#         cnt = 1
#
# print(mx)


# with open('17.txt') as f:
#     data = [int(x) for x in f.readlines()]
#
# mx = max(i for i in data if len(str(i)) == 2)
# ans = []
# for i in range(len(data) - 1):
#     x, y = data[i], data[i + 1]
#     c1 = len(str(x)) == 2 or len(str(y)) == 2
#     c2 = x + y <= mx
#     if c1 and c2:
#         ans.append(x + y)
#
# print(len(ans), max(ans))


# from sys import setrecursionlimit
#
# setrecursionlimit(20000)
#
#
# def f(n):
#     if n > 3000:
#         return n
#     return f(n + 2) + 2
#
#
# print(f(40) - f(43))


# for n in range(1000):
#     s = '1' + '7' * n
#     while '17' in s or '377' in s or '777' in s:
#         if '17' in s:
#             s = s.replace('17', '1', 1)
#         if '377' in s:
#             s = s.replace('377', '73', 1)
#         if '777' in s:
#             s = s.replace('777', '3', 1)
#
#     if s.count('3') == 2:
#         print(n)
#         break


# from itertools import product
#
# for x, y, z, w in product((0, 1), repeat=4):
#     f = (z == (not y)) and (not x or y) and w
#     if f:
#         print(z, x, w, y)


# for n in range(2, 1000):
#     b = bin(n)[2:]
#     if n % 2 == 0:
#         tmp = list(i * 2 for i in b)
#         b = ''.join(i for i in tmp)
#     else:
#         b = list(int(not (int(i))) for i in b)
#         b.remove(0)
#         s = ''
#         for i in b:
#             s += str(i)
#         tmp = list(i * 2 for i in s)
#         b = ''.join(i for i in tmp)
#     r = int(b, 2)
#     if r > 60:
#         print(n)
#         break


# from turtle import *
#
# tracer(0)
# screensize(5000, 5000)
# r = 25
#
# for i in range(2):
#     fd(5 * r)
#     rt(90)
#     fd(11 * r)
#     rt(90)
#
# up()
# fd(-4 * r)
# rt(90)
# fd(6 * r)
# lt(90)
# down()
# for i in range(2):
#     fd(42 * r)
#     rt(90)
#     fd(63 * r)
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
# cnt = 0
# for x in product(sorted('ПРОЛИВ'), repeat=6):
#     s = ''.join(x)
#     if s.count('П') != 0:
#         cnt += 1
# print(cnt)


# with open('27_B.txt') as f:
#     n = int(f.readline())
#     d = dict()
#     for i in range(n):
#         x = int(f.readline())
#         if x % 7 not in d.keys():
#             d[x % 7] = []
#         else:
#             d[x % 7].append(x)
