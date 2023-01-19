# Примеры

## №4987 Кабанов

> Среди натуральных чисел, не превышающих 10^9, найдите все числа, соответствующие
> маске 23?456?89 и делящиеся на 17 без остатка.

```python
from fnmatch import fnmatch

for x in range(0, 10 ** 9, 17):
    if fnmatch(str(x), '23?456?89'):
        print(x, x // 17)
```

## №5281 Агафонцев

> Найдите наименшие 7 чисел, удовлетворяющих маске ?8*8*8?8 и при этом кратных 6,7 и 8.
> Выведите эти числа в порядке возрастания, справа от каждого числа выведите сумму его делителей.

```python
from fnmatch import fnmatch


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d


for x in range(0, 10 ** 7):
    if fnmatch(str(x), '?8*8*?8') and x % 6 == 0 and x % 7 == 0 and x % 8 == 0:
        print(x, sum(div(x)))
```

## №5031 Михлин

> Найдите все числа, делящиеся нацело на 76_16, шестнадцатиричный код которых соответствует маске 1?DED?CED. В ответе
> запишите найденные числа в десятичной сс в порядке убывания, а справа от каждого числа - частное от деления на 76_16.

```python
ans = []
for x in '0123456789abcdef':
    for y in '0123456789abcdef':
        num = int(f'1{x}ded{y}ced', 16)
        base = int('79', 16)
        if num % base == 0:
            ans += [(num, num // base)]

for i in ans[::-1]:
    print(*i)
```

## №5620 Багдасарян

```python
from fnmatch import fnmatch

for x in range(0, 10 ** 8, 2023):
    if fnmatch(str(x), '11[02468]??[13579]11'):
        print(x, x // 2023)
```