V1 = int(input('Размер '))
pcnt = float(input('Процент '))
tup = int(input('Время на сжатие и распаковку '))
v = 2 ** 22

V2 = pcnt * V1
a = (V2 * 2 ** 23) / v + tup
b = (V1 * 2 ** 23) / v
if a > b:
    print('Б', a - b)
else:
    print('А', b - a)
