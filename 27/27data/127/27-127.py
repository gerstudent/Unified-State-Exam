# Автор: А. Рогов

f = open('27-127b.txt')
n, m = map(int, f.readline().split())

points = dict()
w = [0] * 10**8
for _ in range(n):
	num, k = map(int, f.readline().split())
	points[num] = k
	w[num] = k // 50 + bool(k % 50)
#print(max(points))
start = min(points)
k = 0
k_send = 0
for i in range(start, start - m, -1):
	if i < 0:
		break
	k += w[i]
	k_send += points.get(i, 0)
for i in range(start + 1, start + m + 1):
	k += w[i]
	k_send += points.get(i, 0)
mx = k
mx_send = k_send
for i in range(start + 1, max(points) + 1):
	k -= w[i - m - 1]
	k += w[i + m]
	k_send -= points.get(i - m - 1, 0)
	k_send += points.get(i + m, 0)
	# print(i, k)
	if i not in points:
		continue
	# print(i, k)
	if k_send > mx_send:
		mx_send = k_send
		mx = k
	elif k_send == mx_send and k_send < mx:
		mx = k
print(mx)
