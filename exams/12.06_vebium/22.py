d = {"0": 0}
data = []
with open('22.txt') as f:
    for s in f:
        data.append(s.replace(';', ' ').split())

while len(d) != len(data) + 1:
    for s in data:
        idB, time, idA = s[0], s[1], s[2:]
        if all(sub in d for sub in idA):
            d[idB] = int(time) + max(d[sub] for sub in idA)

print(max(d.values()))
