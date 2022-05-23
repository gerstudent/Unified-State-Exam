# https://www.youtube.com/watch?v=WY64fif5Eyc
# № 2403(тайминг на стриме 53.25): в первой куче (a) было 7 камней, во второй куче (b) было s,
# 1 <= s <= 66 камней. Победителем считается игрок, первым получивший позицию,
# в которой в кучах будет 74 или больше камней.

def f(a, b, c, m):
    if a + b >= 74:
        return c % 2 == m % 2

    if c == m:
        return 0

    lst = [f(a + 2, b, c + 1, m),
           f(a, b + 2, c + 1, m),
           f(a * 2, b, c + 1, m),
           f(a, b * 2, c + 1, m)]

    # Так как по условию Ваня выиграл первым ходом после (!) неудачного (!)
    # хода Пети, то для ответа на 1ый вопрос меняем all на any
    return any(lst) if (c + 1) % 2 == m % 2 else all(lst)

for b in range(1, 67):
    for m in range(1, 5):
        if f(7, b, 0, m):
            if m == 2:
                print('Первый ответ (поменять all на any):', b, m)

            if m == 3:
                print('Второй ответ (в зависимости от условия записывать min или max):', b)

            if m == 4:
                print('Третий ответ (в ответ идет 2 значения):', b)
            break

# Итоговый ответ: 19) 17; 20) 29; 21) 27 30
