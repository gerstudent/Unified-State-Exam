# Чтение данных

```python
with open("26.txt") as f:
    n = int(f.readline())
    data = [int(f.readline()) for i in range(n)]
    x, y = map(int, f.readline().split())
```

```python
with open('26.txt') as f:
    m, n = map(int, f.readline().split())
    a = []
    for i in range(n):
        start, end = map(int, f.readline().split())
        a.append([start, start + end, end])
```

# Багажи

### Первый тип

> (досрок 2023) Входной файл содержит заявки пассажиров, желающих сдать свой багаж в камеру хранения. В заявке указаны
> время сдачи
> багажа и время освобождения ячейки (в минутах от начала суток). Багаж одного пассажира размещается в одной свободной
> ячейке с минимальным номером. Ячейки пронумерованы начиная с единицы. Размещение багажа в ячейке или её освобождение
> происходит в течение 1 мин. Багаж можно поместить в только что освобождённую ячейку начиная со следующей минуты. Если
> в момент сдачи багажа свободных ячеек нет, то пассажир уходит. Определите, сколько пассажиров сможет сдать свой багаж
> в течение 24 ч и какой номер будет иметь ячейка, которую займут последней. Если таких ячеек несколько, укажите
> минимальный номер ячейки.

```python
with open('26_8168.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = []
    for i in f:
        a.append([int(x) for x in i.split()])

a.sort()
cells = [-1] * k

cnt_pas = 0
last_start = -1
last_num = -1

for pas in a:
    start = pas[0]
    end = pas[1]
    for i in range(k):
        if cells[i] <= start:
            cells[i] = end + 1
            cnt_pas += 1
            if start > last_start:
                last_start = start
                last_num = i + 1
            break

print(cnt_pas, last_num)
```

### Второй вариант решения

```python
with open('26_8168.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = []
    for i in range(n):
        st, end = map(int, f.readline().split())
        a.append([st, end])

a.sort()
cells = [0] * (k + 1)
cnt_pas = 0
last_cell = 0

for i in range(n):
    start, end = a[i]
    for j in range(1, k + 1):
        if cells[j] < start:
            cells[j] = end
            cnt_pas += 1
            last_cell = j
            break

print(cnt_pas, last_cell)
```

### Второй тип

> (8168) Определите, сколько всего пассажиров не смогут оставить свой багаж в ячейках за 24 часа и общее время, в
> течение которого все ячейки будут заняты (без учета времени на разгрузку ячейки). Гарантируется, что все пассажиры,
> сдавшие багаж, заберут его в пределах 24 часов.

```python
with open('26_8168.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = []
    for i in range(n):
        a.append([int(x) for x in f.readline().split()])

a.sort()
cells_time = [0] * k
cells_not_time = [0] * k

cnt_not_save = 0
cnt_save = 0
all_time = 0

for time in range(1441):
    for i in range(k):
        if cells_time[i] == time:
            cells_time[i] = 0
        if cells_not_time[i] == time:
            cells_not_time[i] = 0

    if 0 not in cells_not_time:
        all_time += 1

    for start, end in a:
        if time == start:
            if 0 in cells_time:
                i = cells_time.index(0)
                cells_time[i] = time + end + 1
                cells_not_time[i] = time + end
                cnt_save += 1
            else:
                cnt_not_save += 1

print(cnt_not_save, all_time)
```

### Третий тип

> Определите, сколько пассажиров сможет сдать свой багаж в течение 24 ч и номер ячейки, которая была заполнена багажом
> наибольшее количество времени. Если таких ячеек несколько, укажите минимальный номер ячейки. Пассажиры обслуживаются в
> порядке их прихода к камере хранения. Если несколько пассажиров хотят сдать багаж в одно и то же время, а свободная
> ячейка только одна, то в таком случае багаж сдаёт пассажир, который освободит ячейку раньше других.

```python
with open('3_26.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = []
    for i in range(n):
        a.append([int(x) for x in f.readline().split()])

a.sort()
cells = [0] * k
cells_time = [0] * k
cnt_pas = 0
last_start = -1

for pas in a:
    start = pas[0]
    end = pas[1]
    for i in range(k):
        if cells[i] <= start:
            cells[i] = end + 1
            cnt_pas += 1
            cells_time[i] += (end - start)
            break

print(cnt_pas, cells_time.index(max(cells_time)) + 1)
```

### Четвёртый тип

> Определите, сколько пассажиров сможет сдать свой багаж в течение 24 ч и суммарное время в минутах на протяжении,
> которого хотя бы в одной ячейке будет находиться багаж. Если несколько пассажиров пришли в одно время к одной
> свободной ячейке, то багаж кладёт тот, время возвращения багажа которого меньше.

```python
with open('3_26.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = []
    for i in range(n):
        a.append([int(x) for x in f.readline().split()])

a.sort()
cells = [0] * k
c = [0] * k
cnt_pas = 0
last_start = -1
minutes = [0] * 1442

for pas in a:
    start = pas[0]
    end = pas[1]
    for i in range(k):
        if cells[i] <= start:
            cells[i] = end + 1
            cnt_pas += 1
            for m in range(start, end):
                minutes[m] += 1
            break

mx_cnt, idx = 0, -1
for i in range(1441):
    if minutes[i] >= mx_cnt:
        mx_cnt = minutes[i]
        idx = i

print(cnt_pas, idx)
```

## Счёт времени

> Определите, сколько пассажиров сможет сдать свой багаж в течение 24 ч и суммарное время в минутах на протяжении,
> которого хотя бы в одной ячейке будет находиться багаж.

```python
with open('3_26.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = []
    for i in f:
        a.append([int(x) for x in i.split()])

a.sort()
cells = [0] * k
time = {minute: 0 for minute in range(1, 1441)}
cnt_pas = 0

for pas in a:
    start = pas[0]
    end = pas[1]
    for i in range(k):
        if cells[i] <= start:
            cells[i] = end + 1
            cnt_pas += 1
            for minute in range(start, end):
                time[minute] += 1
            break

print(cnt_pas, len([i for i in time if time[i] > 0]))
```

# Парковка

> Определите количество микроавтобусов, которые смогут припарковаться, и общее количество автомобилей (как легковых, так
> и микроавтобусов), которые уедут из-за отсутствия мест.

```python
with open('26-119.txt') as f:
    n, l, m = map(int, f.readline().split())
    a = []
    for i in range(n):
        start, duration, type = f.readline().split()
        a.append([int(start), int(start) + int(duration), type])

a.sort()
# первые 0..l - 1 места для легковых
# следующие l...l + m места для минивенов
park = [0] * (l + m)
bus = 0
leave = 0
for i in range(n):
    start, end, type = a[i]
    if type == 'A':
        for j in range(l + m):
            if park[j] <= start:
                park[j] = end
                break
        else:
            leave += 1

    if type == 'B':
        for j in range(l, l + m):
            if park[j] <= start:
                park[j] = end
                bus += 1
                break
        else:
            leave += 1

print(bus, leave)
```

# Банкоматы

> Определите наибольшее количество клиентов, которые были обслужены одним банкоматом за 24 часа, и время начала
> обслуживания последнего клиента. Последним обслуженным клиентом считается тот, который подошёл к любому банкомату до
> окончания суток (его обслуживание могло закончиться в следующие сутки).

```python
with open('26-112.txt') as f:
    m, n = map(int, f.readline().split())
    a = []
    for i in range(n):
        start, end = map(int, f.readline().split())
        a.append([start, start + end, end])

a.sort(key=lambda x: x[0])
bank = [0] * m
bank_cnt = [0] * m
last = 0

for i in range(n):
    start, end, duration = a[i]

    # проверяем: есть ли свободные автоматы
    for j in range(m):
        if bank[j] <= start:
            bank[j] = end
            if start <= 1440:
                bank_cnt[j] += 1
                last = start
            break

    # иначе клиент ждёт пока
    # не освободится один из банкоматов
    else:
        mn = min(bank)
        for j in range(m):
            if bank[j] == mn:
                if bank[j] <= 1440:
                    bank_cnt[j] += 1
                    last = bank[j]
                bank[j] = bank[j] + duration
                break

print(max(bank_cnt), last)
```

# Гномы

> В одной волшебной местности живут гномы, которые любят варить зелья в магических котлах. Всего есть P котлов, они
> пронумерованы, в начальный момент все они свободны. Гномы варят зелья в порядке общей очереди. Первый в очереди гном,
> желающий сварить зелье, подходит к свободному котлу с наименьшим номером. Если котел ранее не использовался, гном
> может
> начать варить зелье сразу, а если уже использовался – только через две минуты после того, как он подошел к такому
> котлу.
> Одна порция зелья варится 1 минуту.
> На заварку одной порции зелья гном тратит две единицы маны (магической энергии для заварки зелий). Если в один момент
> подошли несколько гномов, то варить зелье идёт тот, у кого запас маны меньше. Гном будет варить зелья, пока у него
> достаточно маны для их заварки. Гном, у которого осталось меньше двух единиц маны, не может сварить зелье и уходит.
> Известно время в минутах от начала суток, когда каждый гном подошёл к котлам, и количество маны у гнома. Определите,
> сколько порций зелья сварят гномы за сутки, и какое наибольшее количество порция зелья смог сварить один гном.

```python
with open('26-125.txt') as f:
    d, p = map(int, f.readline().split())
    a = []
    for i in range(d):
        start, mana = map(int, f.readline().split())
        if mana > 1:
            a.append([start, start + mana // 2, mana // 2])

a.sort()
kot = [0] * p
cnt = 0
max_zel = 0
for i in range(len(a)):
    start, end, zel = a[i]
    for j in range(p):
        if kot[j] <= start:
            kot[j] = end if kot[j] == 0 else end + 2
            if kot[j] > 1440:
                zel -= kot[j] - 1440
            cnt += zel
            max_zel = max(max_zel, zel)
            break
print(cnt, max_zel)
```

# Отель и дома

> Турист всегда заселяется в первый свободный домик ближайшей к морю линии, где есть свободные домики. Определить
> максимальный номер линии, в которой будет заселяться хотя бы один домик и количество заселенных домиков в следующий
> час
> после заселения последнего туриста.

```python
from math import ceil

with open('26-122.txt') as f:
    k, n = map(int, f.readline().split())
    a = []
    for i in range(n):
        start, end = map(int, f.readline().split())
        a.append([start, end])

a.sort()
houses = [0] * 1000
last = 0
for i in range(n):
    start, end = a[i]
    for j in range(1000):
        if houses[j] + 1 <= start:
            houses[j] = end
            last = len([x for x in houses if x > start])
            break

houses = [x for x in houses if x != 0]
print(ceil(len(houses) / k), last)
```

# Временная линия

> Автомат фиксирует пассажиров некоторого автобуса по ходу рейса. У каждого пассажира фиксируется время входа и выхода с
> момента начала рейса. Необходимо узнать максимальное количество пассажиров, одновременно находящихся в автобусе, и
> общее время, когда в автобусе был хотя бы один пассажир. Временем входа и выхода в автобус пренебречь.

```python
with open('26-75.txt') as f:
    n = int(f.readline())
    a = [0] * 1_000_000
    for i in range(n):
        start, end = map(int, f.readline().split())
        a[start] += 1
        a[end] -= 1

cnt_pas = 0
ans = 0
mx = 0
for i in range(10 ** 6):
    cnt_pas += a[i]
    mx = max(mx, cnt_pas)
    if cnt_pas > 0:
        ans += 1

print(mx, ans)
```

# Конференц зал

```python
with open('26.txt') as f:
    n = int(f.readline())
    a = []
    for i in range(n):
        start, end = map(int, f.readline().split())
        a.append([start, end])

a.sort(key=lambda x: x[1])
cnt = 0
limit = 0
for i in range(n):
    start, end = a[i]
    if start >= limit:
        limit = end
        cnt += 1

print(cnt)
```
