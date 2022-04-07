# номер 3084 (А. Кабанов)

def f(s, c, m):
    if 43 <= s <= 72:
        return c % 2 == m % 2

    if s > 72:
        return c % 2 != m % 2

    if c == m:
        return 0

    lst = [f(s + 1, c + 1, m), f(s * 2, c + 1, m), f(s * 3, c + 1, m)]

    return any(lst) if (c + 1) % 2 == m % 2 else all(lst)

# m = 1 --- первый ход Пети
# m = 2 --- первый ход Вани
# m = 3 --- второй ход Пети и тд.
for s in range(1, 43):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 2:
                print("Первый ответ:", s, m)
            if m == 3:
                print("Второй ответ:", s, m)
            if m == 4:
                print("Третий ответ:", s, m)
            break
