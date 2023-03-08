# Автор: М. Фирсов

def check(n):
    for i in range(len(n)):
        if n[i][0] < 0:
            n[i][0] = 0
    return n


with open("27-113b.txt") as file:
    n = int(file.readline()) - 1
    s = [[1, 15], [11, 40], [21, 70]]
    number = int(file.readline())
    for i in range(n):
        new_number = int(file.readline());
        r = new_number - number
        number = new_number

        s = [[prev_pos - r, prev_sum] for prev_pos, prev_sum in s]
        s = check(s)

        s = {y[0]: y for y in sorted(s, reverse = True)}
        if 0 in s:
            sum = s[0][1]
            s[0] = [1, sum + 15]
            s = list(s.values()) + [[11, sum + 40], [21, sum + 70]]
        else: s = list(s.values())

    print(min([i[1] for i in s]))