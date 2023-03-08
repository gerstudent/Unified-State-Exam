# 5

for n in range(0, 400):
    b = bin(n)[2:]
    for i in range(2):
        sm = sum(map(int, str(n)))
        if sm % 2 != 0:
            b = b + '1'
        else:
            b = b + '0'
    res = int(b, 2)
    if res > 1028:
        print(res)
        break

# 6

from turtle import *

tracer(0)
screensize(2000, 2000)
r = 40

for i in range(4):
    fd(7 * r)
    rt(90)
    fd(7 * r)
    lt(90)
    fd(7 * r)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * r, y * r)
        dot(3, "blue")

exitonclick()
update()

# 8
from itertools import product

cnt = 0
for x in product("ВЕРОНИКА", repeat=6):
    s = ''.join(x)
    glc = s.count('Е') + s.count('О') + s.count('И') + s.count('А')
    soglc = s.count('В') + s.count('Р') + s.count('Н') + s.count('К')
    if glc > soglc:
        cnt += 1

print(cnt)


# 15

def d(x, d):
    return x % d == 0


def nd(x, d):
    return x % d != 0


def f(x, y, a):
    return (d(144, x) <= (not d(x, y))) or (x + y > 100) or (a - x > y)


for a in range(1, 1001):
    if all(f(x, y, a) == 1 for x in range(1, 500) for y in range(1, 500)):
        print(a)
        break
