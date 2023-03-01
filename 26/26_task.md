# Чтение данных

```python
with open("26.txt") as f:
    n = int(f.readline())
    data = [int(f.readline()) for i in range(n)]
    x, y = map(int, f.readline().split())
```