from math import log2, ceil, floor

# величина, которую требуется найти = 0

alph = int(input('Мощность алфавита: '))
symb = int(input('Количество символов: '))
obj = int(input('Количество объектов: '))
memory = int(input('Память(в байтах): '))
dop = int(input('Доп. сведения(в байтах): '))

i = ceil(log2(alph))  # Бит на символ
user = ceil((symb * i) / 8) + dop  # Память на пользователя

if memory == 0:
    memory = user * obj
    print("Память (в байтах) на всех:", memory)
    print("Память (в Кб) на всех:", memory // 1024)

if obj == 0:
    obj = floor(memory / user)
    print("Количество объектов:", obj)
