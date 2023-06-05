# Формулировки

1. Найдите минимальную длину линии, которой можно нарисовать эту фигуру.

> Считаем периметр получившейся фигуры по квадратам.

# Задание системы координат

```python
up()
goto(-50 * r, 0)
down()
goto(50 * r, 0)
up()
goto(0, -50 * r)
down()
goto(0, 50 * r)
up()
```

# Черепаха

## Задача №27

> Повтори 7 (Направо 90 Вперёд 4 Повтори 2 (Налево 90 Вперёд 4))

```python
from turtle import *

screensize(8000, 8000)
tracer(0)
r = 25

# Повтори
for i in range(7):
    rt(90)
    fd(4 * r)
    for j in range(2):
        lt(90)
        fd(4 * r)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * r, y * r)
        dot(3, "blue")

update()
exitonclick()
```

## Задача №42

```python
from turtle import *

tracer(0)
screensize(8000, 8000)
r = 10

for i in range(10):
    for j in range(3):
        fd(10 * r)
        rt(90)
        fd(10 * r)
        rt(270)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * r, y * r)
        dot(3, "blue")

update()
exitonclick()
```

# Чертежник

## Задача №9 (Сколько различных точек)

```python
from turtle import *

tracer(0)
screensize(3000, 3000)
r = 25


# сместиться
def move(a, b):
    return goto(xcor() + a * r, ycor() + b * r)


for i in range(7):
    move(6, -9)
    move(-6, 2)
    move(12, 3)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * r, y * r)
        dot(3, "blue")

update()
exitonclick()
```
