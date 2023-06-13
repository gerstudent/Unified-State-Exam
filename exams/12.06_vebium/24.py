with open('24_9441.txt') as f:
    s = f.readline()

s = s.split('A')
print(max(len(c) for c in s))
