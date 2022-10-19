# Решение вручную (множества и отрезки)

1. Преобразовать выражение до "читаемой" импликации
2. Записать критерий истинности и найти ответ

# Делимость (порязрядная конъюнкция решается аналогично)

## Задача 1

> Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого
> наименьшего натурального числа А формула f тождественно истинна (то есть принимает значение 1 при любом натуральном
> значении переменной x)?

## Решение задачи 1

```python
def d(x, d):
    return x % d == 0


def nd(x, d):
    return x % d != 0


def f(x, a):
    return d(a, 35) and (d(730, x) <= (nd(a, x) <= nd(110, x)))


cnt = 0
for a in range(1, 1001):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        cnt += 1

print(cnt)
```

# Множества

## A min (... <= A):

1. Изначально A пустое
2. Кладем все x, в которых f ложна

## A max (A <= ...):

1. Изначально A бесконечно большое
2. Убираем все x, в которых выражение ложно

## Наименьшее

> Элементами множества A являются натуральные числа. Известно, что выражение f истинно. Определите наименьшее возможное
> значение суммы элементов множества A.

```python
p = {1, 3, 5, 7, 9, 11}
q = {3, 6, 9, 12}
a = set()


def f(x):
    return ((x in p) <= (x not in q)) or (x in a)


for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)

print(sum(a))
```

## Наибольшее

```python
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
a = set(range(1, 1000))


def f(x):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))


for x in range(1, 1000):
    if f(x) == 0:
        a.remove(x)

print(len(a))
```

# Отрезки

## Наибольший

```python
def p(x):
    return 550 <= x <= 800


def q(x):
    return 200 <= x <= 1050


def f(x, a1, a2):
    return q(x) <= ((p(x) == q(x)) or ((not (p(x))) <= (a1 <= x <= a2)))


m = 0
for a1 in range(500, 1200):
    for a2 in range(a1 + 1, 1200):
        if all(f(x, a1, a2) == 1 for x in range(500, 1200)):
            m = max(m, a2 - a1)

print(m / 10)
```

## Наименьший

```python
p1 = 10
p2 = 20
q1 = 35
q2 = 45


def f(x, a1, a2):
    P = p1 <= x <= p2
    Q = q1 <= x <= q2
    A = a1 <= x <= a2
    return ((not P) <= Q) and (not A)


m = []
for i in range(500):
    for j in range(500):
        if all(f(x, i, j) == 1 for x in range(500)):
            m.append(j - i)

print(min(m, default=0))
```

# С промежутком (№412 Поляков)

```python
def Del(x, d):  return x % d == 0


def nDel(x, d):
    return x % d != 0


def f(x, A):
    return Del(A, 35) and (Del(730, x) <= (nDel(A, x) <= nDel(110, x)))


count = 0
for A in range(1, 1001):
    OK = 1
    for x in range(1, 30000):
        if not f(x, A):
            OK = 0
            break
    if OK:
        count += 1

print(count)
```

