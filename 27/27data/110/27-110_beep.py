# Автор: beep

n = None
k = None
buff = []

with open("27-110b.txt") as f:

	n, k = map(int, f.readline().split())

	buff.append((k, 0))

	for i, x in enumerate(f):

		a, b = list(map(int, x.split()))
		buffT = []

		for case in buff:

			buffT.append(case)
			buffT.append((k, case[1] + b))
			if case[0] > 0: buffT.append((case[0] - 1, case[1] + a))

		buff = []
		buffT.sort(key=lambda x: (-x[1], -x[0]))
		border = None

		for case in buffT:
			if not border or case[0] > border:
				buff.append(case)
				border = case[0]


buff.sort(key=lambda x: (-x[1], x[0]))
print(buff[0][1])