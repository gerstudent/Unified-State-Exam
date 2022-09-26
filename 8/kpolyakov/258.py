from itertools import product

word = 'АИКЛМЬ'
cnt = 0
w = list(''.join(i) for i in product(word, repeat=6))


def valid(s):
    return s[0] == 'К' and s[-1] == 'Ь' \
           and len(set(s)) == 6 and \
           w.index(s[::-1]) - w.index(s) == 26655


for i, elem in enumerate(w, start=1):
    if valid(elem):
        print(elem, sum(map(int, str(i))))
        break
