from math import log2, ceil, floor

N = int(input('Мощность алфавита: '))
n = int(input('Количество символов: '))
obj = int(input('Количество объектов: '))
m = int(input('Память(в байтах): '))
dop = int(input('Доп. сведения(в байтах): '))

i = ceil(log2(N))  # Бит на символ
user = ceil((n * i) / 8) + dop
print(user)
if m == 0:
    m = user * obj
    print(m)
if obj == 0:
    obj = floor(m / user)
    print(obj)
