# Первый вариант

```python
V = int(input('Размер '))
pcnt1 = float(input('Процент 1 '))
pcnt2 = float(input('Процент 2 '))
tup1 = int(input('Время 1 на сжатие и распаковку '))
tup2 = int(input('Время 2 на сжатие и распаковку '))
v = 2 ** 20

V1 = pcnt1 * V
V2 = pcnt2 * V
a = (V1 * 2 ** 23) / v + tup1
b = (V2 * 2 ** 23) / v + tup2
if a > b:
    print('Б', a - b)
else:
    print('А', b - a)
```

# Второй вариант

```python
V = int(input('Размер '))
pcnt = float(input('Процент '))
tup = int(input('Время на сжатие и распаковку '))
v = 2 ** 24

V2 = pcnt * V
a = (V2 * 2 ** 23) / v + tup
b = (V * 2 ** 23) / v
if a > b:
    print('Б', a - b)
else:
    print('А', b - a)
```