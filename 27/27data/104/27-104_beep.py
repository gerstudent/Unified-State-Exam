# Автор: beep

n = None
m = 4043520
mul = 1
buff = []
count = 0

with open("27-104b.txt", "r") as f:
	n = int(f.readline())
	for i, x in enumerate(f):
		x = int(x)
		mul *= x
		buff.append(x)
		while m % mul != 0:
			mul //= buff.pop(0)
		count += len(buff)

print(count)

"""
Если заботиться о переполнении и исключить встроенную длинную математику
(что не сделано в варианте решения "27-104_bad.py"), то можно фильтровать
накопление произведения через квадратный корень от m:
"""

n = None
m = 4043520
mul = 1
buff = []
count = 0
border = round(m**0.5)

with open("27-104b.txt", "r") as f:
	n = int(f.readline())
	for i, x in enumerate(f):
		x = int(x)
		if x > m:
			buff = []
			mul = 1
			continue
		if x > border and mul > border:
			while mul > border:
				mul //= buff.pop(0)
		mul *= x
		buff.append(x)
		while m % mul != 0:
			mul //= buff.pop(0)
		count += len(buff)

print(count)