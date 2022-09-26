from itertools import product

words = [''.join(x) for x in product('СТЕПУХА', repeat=4)]
words = words[1000:]
cnt = 0

for w in words:
    if all(c1 != c2 for c1, c2 in zip(w, w[1:])):
        cnt += 1

print(cnt)
