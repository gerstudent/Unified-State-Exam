# Автор: beep

#----------------------------------------------
# Вариант 1. С длинной математикой:
#----------------------------------------------

n = None
mul = 1
m = 8_023_320
buff = []
lMax = None
iMin = None

with open('27-106b.txt', "r") as f:

	n = int(f.readline())

	for i, x in enumerate(f):

		x = int(x)

		mul *= x
		buff.append((x, i))
		while m % mul != 0:
			mul //= buff.pop(0)[0]

		if not buff: continue
		l = len(buff)
		if lMax is None or l > lMax:
			lMax = l
			iMin = buff[0][1]

print(iMin + 1)

#----------------------------------------------
# Вариант 2. Без длинной математики
#----------------------------------------------

n = None
mul = 1
m = 8_023_320
buff = []
lMax = None
iMin = None

with open('27-106b.txt', "r") as f:

	n = int(f.readline())

	for i, x in enumerate(f):

		x = int(x)

		if x > m:
			buff = []
			mul = 1
			continue

		border = m / x
		while mul > border:
			mul //= buff.pop(0)[0]

		mul *= x
		buff.append((x, i))
		while m % mul != 0:
			mul //= buff.pop(0)[0]

		if not buff: continue
		l = len(buff)
		if lMax is None or l > lMax:
			lMax = l
			iMin = buff[0][1]

print(iMin + 1)
