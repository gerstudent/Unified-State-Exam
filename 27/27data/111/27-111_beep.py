# Автор: beep

n = k = None

with open("27-111b.txt", "r") as f:
    n, k = map(int, f.readline().split())
    data = []
    for i, x in enumerate(f):
      data.append(int(x))

data = data + data
s = 0
cash = {0 : -1}
lMin = None

for i, x in enumerate(data):
	s += x
	cash[s ] = i
	delta = s - k
	if delta in cash:
        p = cash[delta]
	else:
        continue
	if p >= n: break
	lT = i - p
	if lMin is None or lT < lMin:
        lMin = lT

print(lMin)
