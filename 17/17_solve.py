# 14 (1) (333)

with open('17-333.txt', 'r') as f:
    data = [int(n) for n in f.readlines()]


def arithmetic(lst):
    n = 0
    sum = 0
    for i in lst:
        if len(str(i)) == 4:
            n += 1
            sum += i

    return sum / n


m = -10 ** 6
cnt = 0
arithm = arithmetic(data)
for i in range(0, len(data) - 1):
    num1 = data[i]
    num2 = data[i + 1]
    sum_num = num1 + num2
    sum_digits = sum(map(int, str(num1))) + sum(map(int, str(num2)))
    if data.count(sum_num) == 0 and sum_num < arithm:
        cnt += 1
        m = max(m, sum_digits)

print(cnt, m)

# 15 (1)

from collections import Counter

with open('17-332.txt') as f:
    data = [int(i) for i in f.readlines()]

n = 0
sm = 0
for i in data:
    if i % 17 == 0:
        n += 1
        sm += i

arithm = sm / n

cnt = 0
ans = []
d = {}
for i in range(0, len(data) - 3):
    a, b, c = data[i], data[i + 1], data[i + 2]
    sumA = sum(map(int, str(a)))
    sumB = sum(map(int, str(b)))
    sumC = sum(map(int, str(c)))
    if sumA == sumC and b < arithm:
        cnt += 1
        ans.append(sumB)

print(cnt, Counter(ans).most_common(1))
