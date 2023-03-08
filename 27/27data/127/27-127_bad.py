# Автор: А. Рогов

f = open('27-127a.txt')
n, m = map(int, f.readline().split())

count = 10000000
data = [0] * count
for i in range(n):
  i, j = map(int, f.readline().split())
  data[i - 1] = j

mx = 0
mx_send = 0
for i in range(count):
	k = 0
	k_send = 0
	if data[i] == 0:
		continue
	k += data[i] // 50 + bool(data[i] % 50)
	k_send += data[i]
	for j in range(i - 1, i - m - 1, -1):
		if j >= 0:
			k += data[j] // 50 + bool(data[j] % 50)
			k_send += data[j]
	for j in range(i + 1, i + m + 1):
		if j < count:
			k += data[j] // 50 + bool(data[j] % 50)
			k_send += data[j]
	# print(i + 1, k)
	if k_send > mx_send:
		mx_send = k_send
		mx = k
	elif k_send == mx_send and k_send < mx:
		mx = k
print(mx)
