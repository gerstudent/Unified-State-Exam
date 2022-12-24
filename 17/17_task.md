# Как читать числа из файла

1. Вариант 1

```python
a = [int(x) for x in open('FILENAME.txt')]
```

2. Вариант 2

```python
with open('FILENAME.txt', 'r') as f:
    A = [int(n) for n in f.readlines()]
```

