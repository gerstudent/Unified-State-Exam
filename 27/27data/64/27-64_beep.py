# Автор: beep

n = -1
res = [[] for i in range(3)]
s1 = 0
s2 = 0
s3 = 0

with open("27-64a.txt", "r") as f:

	n = int(f.readline())

	for i, x in enumerate(f):

		arr = list(map(int, x.split()))

		if arr[0] % 2 != 1: continue

		arr.sort()

		a, b = arr
		c = a + b

		bit1 = a % 2
		bit2 = b % 2

		s1 += a
		s2 += b
		s3 += c

		index = bit1 + (bit2 << 1) - 1
		res[index].append(c)

for arr in res:
	arr.sort()

bit1 = s1 % 2
bit2 = s2 % 2
flag = (bit1 << 1) + bit2

if flag == 1:
	print(s3)

else:

	if flag: res[0], res[1] = res[1], res[0]
	if flag != 2: res[1], res[2] = res[2], res[1]

	delta = []
	if res[2]: delta.append(res[2][0])
	if res[0] and res[1]: delta.append(res[0][0] + res[1][0])

	if delta:
		print(s3 - min(delta))
	else:
		print("oops!", flag)