from numba import njit


@njit
def calc(x, y):
    c1 = x > 50000 and y > 50000
    c2 = (x + y) % 80 == 0
    return c1 and c2


for c in ['A', 'B']:
    with open(f'27{c}_2733.txt') as f:
        n = int(f.readline())
        cnt = 0
        data = [int(x) for x in f.readlines()]
        for i in range(n):
            for j in range(i + 1, n):
                c1 = data[i] > 50000 or data[j] > 50000
                if (data[i] + data[j]) % 80 == 0 and c1:
                    cnt += 1

    print(cnt, end=' ')
