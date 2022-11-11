# Формулировки

> Определите сумму чисел, которые выведет процедура f(30).

```python
def f(n):
    s = 0
    s += n + 1
    if n > 1:
        s += n + 5
        s += f(n - 1)
        s += f(n - 2)
    return s


print(f(30))
```

> Назовите минимальное значение n, для которого F(n) > 1000. (Необходимо обрабатывать исключение RecursionError)

```python
for n in range(1, 1000):
    try:
        if f(n) > 1000:
            print(n)
            break
    except RecursionError:
        print("fail")
```

# Мемоизация рекурсии (Кэширование)

## Рукописный кэш

> Алгоритм вычисления функций F(n) и G(n) задан следующими отношениями. Чему равна сумма цифр значения функции F(50)?

```python
cache = {}


def f(n):
    if n not in cache:
        if n == 1:
            cache[n] = 1
        else:
            cache[n] = f(n - 1) + 3 * g(n - 1)
    return cache[n]


def g(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)


print(sum(int(i) for i in str(f(50))))
```

## Встроенное кэширование

```python
from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n - 1) + 3 * g(n - 1)


def g(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)


print(sum(int(i) for i in str(f(50))))
```