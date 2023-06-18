# Прототипы

## 1

> 8480
> Текстовый файл состоит не более чем из 107 прописных латинских букв. Определите максимальное количество идущих подряд
> символов, среди которых не содержится два символа из набора букв A, B, C в различных комбинациях (с учётом
> повторений), стоящих рядом.

```python
with open('24_8480.txt') as f:
    s = f.readline()

s = s.replace('B', 'A').replace('C', 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')

print(max(len(c) for c in s.split()))
```

```python
from itertools import product

with open('24_8480.txt') as f:
    s = f.readline()

for i in product('ABC', repeat=2):
    k = ''.join(i)
    s = s.replace(k, k[0] + ' ' + k[1])

s = s.split()
print(len(max(s, key=len)))
```

## 2

> Текстовый файл состоит не более чем из 106 символов и содержит только буквы латинского алфавита и десятичные цифры.
> Найдите максимальную длину подстроки, ограниченной с двух сторон одним и тем же символом и не содержащей этого символа
> между ними. В ответе укажите длину найденной строки, включая граничные символы. Например, для строки ABCDABECD ответом
> будет 6.

```python
with open('24_7891.txt') as f:
    s = f.readline()

mx = 0
for i in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM':
    m = max(len(c) for c in s.split(i))
    mx = max(m, mx)

print(mx + 2)
```

## 3

# Разбивка символов

```python
s = s.replace('A', ' ').replace('C', ' ')
print(max(len(c) for c in s.split()))
```

# Перебор вариантов

```python
c = mx = 0
for i in range(len(s)):
    if s[i] in 'ACDF':
        c += 1
        mx = max(mx, c)
    else:
        c = 0
```

# Запретное сочетание

```python
c = mx = 1
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'ST':
        c += 1
        mx = max(mx, c)
    else:
        c = 1

print(mx)
```

- Если заменяется сочетание, в котором первая и последняя буквы совпадают, то
- необходимо использовать while

```python
while 'AAA' in s:
    s = s.replace('AAA', 'AA AA')
```

# Сравнение соседних символов

> Найдите длину самой длинной подцепочки, состоящей из одинаковых символов.
> Выведите сначала символ. Если несколько подходящих подцепочек, выведите первую из них.

```python
c = mx = 1
ch = ''
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
        if c > mx:
            mx = c
            ch = s[i]
    else:
        c = 1
print(ch, mx)
```

> Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

```python
c = mx = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        c += 1
        mx = max(mx, c)
    else:
        c = 1
```

# Возрастание / убывание

> Максимальное количество идущих подряд чисел, расположенных в возрастающем порядке.

```python
c = mx = 1
for i in range(len(s) - 1):
    if s[i + 1] > s[i]:
        c += 1
        mx = max(mx, c)
    else:
        c = 1
```

# Количество пар символов

```python
s = s.replace('ZX', '*').replace('ZY', '*')
s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
```

# Количество троек символов

> Определите максимальное количество идущих подряд символов вида "буква + цифра + цифра"

```python
s = s.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
s = s.replace('A11', '*').replace('A', ' ').replace('1', ' ')
print(max(len(x) for x in s.split()))
```

> Максимальное количество идущих пар символов AA или CC.

```python
c = mx = 0
for j in 0, 1:
    c = 0
    for i in range(j, len(s) - 1, 2):
        if s[i] + s[i + 1] == 'AA' or s[i] + s[i + 1] == 'CC':
            c += 1
            mx = max(mx, c)
        else:
            c = 0
```

# Разбиение по символам

> Определите максимальное количество идущих подряд символов, среди которых ровно две точки.

```python
s = s.split('.')
mx = 0
for i in range(len(s) - 2):
    c = s[i] + '.' + s[i + 1] + '.' + s[i + 2]
    mx = max(mx, len(c))
```

> Определите максимальное количество идущих подряд символов, среди которых
> комбинация символов AB встречается ровно 21 раз.

```python
s = s.split('AB')
mx = 0
for i in range(len(s) - 21):
    c = 44
    for j in range(i, i + 22):
        c += len(s[j])
    mx = max(mx, c)
```

# Поиск минимального четного числа

```python
for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(c, ' ')
s = [int(c) for c in s.split() if int(c) % 2 == 0]
print(min(s))
```

# Максимальная длина последовательности из чередующихся символов E и F.

```python

# запустить 4 раза: 
# 1) for j in range(0, ...) и 'EF' 
# 2) for j in range(1, ...) и 'EF'
# 3) for j in range(0, ...) и 'FE'
# 4) for j in range(1, ...) и 'FE'

with open('24.txt') as f:
    s = f.readline()

mx = 0
for i in s.split('D'):
    cnt = 1
    for j in range(1, len(i) - 1, 2):
        if i[j] + i[j + 1] == 'EF':
            cnt += 2
        else:
            mx = max(cnt, mx)
            cnt = 1
    mx = max(cnt, mx)

print(mx)
```





