# Template

```python
from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = ((w <= y) and ((not x) <= z))
    if f:
        print(x, y, z, w)
```

# Пример записи выражения

+ Выражение: ``((w → y) ∧ (¬ x → z)) → ((z ≡ w) ∨ (y ∧ ¬ x))``
+ Запись в программе: ``((w <= y) and ((not x) <= z)) <= ((z == w) or (y and not x))``
