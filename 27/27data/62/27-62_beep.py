# Автор: beep

n = -1
arr = []

with open("27-62b.txt", "r") as f:
	n = int(f.readline())
	for i, x in enumerate(f):
		x = int(x)
		arr.append(x)

arr.sort()

res = {}
lMax = -1
buff = []
stop = -1

for x in arr:
	for i, y in enumerate(buff):
		step = x - y
		if step > 100:
			stop = i
			continue
		seed = x % step

		if step not in res: res[step] = {}
		if seed not in res[step]: res[step][seed] = {
			"count" : 1,
			"nextX" : x
		}

		if res[step][seed]["nextX"] == x:
			res[step][seed]["count"] += 1
			lMax = max(lMax, res[step][seed]["count"])
		else:
			res[step][seed]["count"] = 2

		res[step][seed]["nextX"] = x + step


	if stop != -1:
		buff = buff[stop + 1 : ]
		stop = -1

	buff.append(x)

print(lMax)

#----------------------------------------
# Второй вариант:
#----------------------------------------

n = -1
arr = []

with open("27-62b.txt", "r") as f:
	n = int(f.readline())
	for i, x in enumerate(f):
		x = int(x)
		arr.append(x)

arr.sort()

res = {}
lMax = -1
buff = []
stop = -1
for x in arr:
	resT = {}
	keys = sorted(res)

	for key in keys:
		if key < x: continue
		delta = 1 if key == x else 0
		for seed in res[key]:
			for step, count in res[key][seed].items():
				keyNew = key + step * delta
				if keyNew not in resT: resT[keyNew] = {}
				if seed not in resT[keyNew]: resT[keyNew][seed] = {}
				resT[keyNew][seed][step] = count + delta
				lMax = max(lMax, resT[keyNew][seed][step])


	for i, y in enumerate(buff):
		step = x - y
		if step > 100:
			stop = i
			continue
		seed = x % step
		keyNew = x + step
		if keyNew not in resT: resT[keyNew] = {}
		if seed not in resT[keyNew]: resT[keyNew][seed] = {}
		if step not in resT[keyNew][seed]: resT[keyNew][seed][step] = 2

	if stop != -1:
		buff = buff[stop + 1 : ]
		stop = -1

	buff.append(x)
	res = resT


print(lMax)