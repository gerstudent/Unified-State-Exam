with open('17_9436.txt') as f:
    data = [int(x) for x in f.readlines()]


def convert(num, to_base=10, from_base=10):
    if isinstance(num, str):  # Если число - строка, то ...
        n = int(num, from_base)  # ... переводим его в нужную систему счисления
    else:
        n = int(num)

    # Перевод десятичной в 'to_base' систему
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Берём алфавит
    if n < to_base:
        return alphabet[n]  # вернуть значения номера в алфавите (остаток от деления)
    else:
        # рекурсивно обратиться к функции нахождения остатка
        return convert(n // to_base, to_base) + alphabet[n % to_base]


ans = []
for i in range(len(data) - 1):
    x, y = data[i], data[i + 1]
    num = convert(abs(x + y), 5, 10)
    c1 = num[-2] == '1' and num[-1] == '4'
    c2 = str(x).count('3') == 2
    if c1 and c2:
        ans.append(x + y)

print(len(ans), max(ans))
