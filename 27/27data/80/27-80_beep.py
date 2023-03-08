# Автор: beep

n = None
k = 3
indexes = []
s = [0]

with open("27-80b.txt") as f:
	n = int(f.readline())
	for i, x in enumerate(f):
		x = int(x)
		if x % 5 == 0: indexes.append(i)
		s.append(s[-1] + x)

s.pop(0)
l = len(indexes)
l -= l % k
sMax = None

for i in range(len(indexes) - l + 1):
	if i == 0:
        tail = 0
	else:
        tail = s[indexes[i - 1]]
	if i + l == len(indexes):
        head = s[-1]
	else:
        head = s[indexes[i + l] - 1]

	sTemp = head - tail
	if sMax is None or sTemp > sMax:
        sMax = sTemp

print(sMax)