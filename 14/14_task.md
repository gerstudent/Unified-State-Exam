# Перевод из десятичной системы в любую другую

```python
def dec_to_base(x, y):
    w = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''

    while x > 0:
        if x % y > 9:
            s += w[x % y - 10]
        else:
            s += str(x % y)
        x //= y
    return s[::-1]
```

# Формулировки

> Значение выражения x записали в системе счисления с основанием base. Сколько цифр num содержится в этой записи?

```python
x = 12345
base = int(input())
num = int(input())

cnt = 0
while x > 0:
    if x % base == num:
        cnt += 1
    x //= base
print(cnt)
```

> (290)(А. Кабанов) Значение выражения $64^{12} – 8^{14} + x$ записали в восьмеричной системе счисления, при этом в
> записи оказалось 12 цифр 7 и одна единица. При каком наименьшем натуральном x это возможно?

```python
for i in range(1, 1000):
    x = 64 ** 12 - 8 ** 14 + i
    cnt1 = 0
    cnt7 = 0
    while x > 0:
        if x % 8 == 7:
            cnt7 += 1
        if x % 8 == 1:
            cnt1 += 1
        x //= 8
    if cnt1 == 1 and cnt7 == 12:
        print(i)
        break
```

> (180)Определите число N, для которого выполняется равенство $214_N = 165_{N+1}$.

```python
for n in range(1, 100):
    try:
        if int('214', n) == int('165', n + 1):
            print(n)
    except:
        ...
```

> (57) Запись числа 338 в системе счисления с основанием N содержит 3 цифры и оканчивается на 2. Чему равно максимально
> возможное основание системы счисления?

```python
for n in range(1, 1000):
    if 338 % n == 2 and n ** 2 <= 338 < n ** 3:
        print(n)
```

# Операнды

## Задача 1

> Операнды арифметического выражения записаны в системе счисления с основанием base. В записи чисел переменной x
> обозначена неизвестная цифра из алфавита base-ричной системы счисления. Определите наименьшее значение x, при котором
> значение данного арифметического выражения кратно num. Для найденного значения x вычислите частное от деления значения
> арифметического выражения на num и укажите его в ответе в десятичной системе счисления.

```python
base = 17
num = 11
for x in '0123456789abcdef':
    a = int(f'9759{x}', base) + int(f'3{x}108', base)
    if a % num == 0:
        print(a // num)
        break
```

## Задача 2 (364 Поляков)

> Операнды арифметического выражения записаны в системе счисления с основанием 55.
> В записи чисел переменной a обозначена неизвестная цифра из алфавита 55-ричной системы счисления. Определите
> наибольшее и наименьшее значение a, при котором значение данного арифметического выражения кратно 29. Для найденных
> значений a найдите модуль разности значений соответствующих выражений.

```python
def f(s, sys, dt):
    cnt = 0
    for i in range(len(s)):
        if s[i] != 'a':
            cnt += int(s[i], 36) * sys ** i
        else:
            cnt += dt * sys ** i

    return cnt


base = 55
num = 29

exp1 = 'ZaYX'[::-1]
exp2 = '2XaX'[::-1]

dig = [i for i in range(base)]
ans = []

for a in dig:
    res = f(exp1, base, a) - f(exp2, base, a)
    if res % num == 0:
        ans.append(res)

print(max(ans) - min(ans))
```

# Задача 3 (363 Поляков)

```python
def f(s, sys, dt):
    cnt = 0
    for i in range(len(s)):
        if s[i] != 'x':
            cnt += int(s[i], 36) * sys ** i
        else:
            cnt += dt * sys ** i

    return cnt


base = 44
num = 42

exp1 = '1x23'[::-1]
exp2 = '32x1'[::-1]

dig = [i for i in range(base)]
ans = []

for a in dig:
    res = f(exp1, base, a) + f(exp2, base, a)
    if res % num == 0:
        ans.append(res // num)

print(max(ans))
```

# Задача 4 (351 Поляков)

```python
for x in '0123456789abc':
    a1 = int(f'{x}1418', 13)
    a2 = int(f'1{x}037', 14)
    a3 = int(f'2{x}209', 19)
    f = a1 + a2 == a3
    if f:
        print(a3)
```
