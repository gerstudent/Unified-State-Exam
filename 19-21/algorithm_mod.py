# Модифицированный (удобный в использовании, но неэффективный) алгоритм, который выводит решение каждой задачи по отдельности.
# №26 Поляков

def f2021(a, b, c, m):
    if a + b >= 79:
        return c % 2 == m % 2

    if c == m:
        return 0

    lst = [f2021(a + 3, b, c + 1, m),
           f2021(a, b + 3, c + 1, m),
           f2021(a * 2, b, c + 1, m),
           f2021(a, b * 2, c + 1, m)
           ]

    return any(lst) if (c + 1) % 2 == m % 2 else all(lst)


def f19(a, b, c, m):
    if a + b >= 79:
        return c % 2 == m % 2

    if c == m:
        return 0

    lst = [f19(a + 3, b, c + 1, m),
           f19(a, b + 3, c + 1, m),
           f19(a * 2, b, c + 1, m),
           f19(a, b * 2, c + 1, m)
           ]

    return any(lst) if (c + 1) % 2 == m % 2 else any(lst)


for b in range(1, 68):
    for m in range(1, 5):
        if f19(9, b, 0, m):
            if m == 2:
                print('Первый ответ (min): ', b, m)
            break

for b in range(1, 68):
    for m in range(1, 5):
        if f2021(9, b, 0, m):
            if m == 3:
                print('Второй ответ (min):', b)
            break

for b in range(1, 68):
    for m in range(1, 5):
        if f2021(9, b, 0, m):
            if m == 4:
                print('Третий ответ:', b)
            break

# Итоговый ответ: 19) 18; 20) 17; 21) 26 27
