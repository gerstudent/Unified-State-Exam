# Автор: beep

n = None
k = None
res = []

with open("27-110b.txt") as f:

	n, k = map(int, f.readline().split())
	res = [[0] * (k + 1) for i in range(2)]

	for i, x in enumerate(f):

		a, b = list(map(int, x.split()))

		for j in range(k + 1):

			res[1][j] = max(res[0][j],
					a + res[0][j - 1] if j
					else b + max(res[0]))

		res[0], res[1] = res[1], res[0]


print(max(res[0]))