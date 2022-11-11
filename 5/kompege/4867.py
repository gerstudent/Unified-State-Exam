def sumEvenNums(n):
    lst = [int(i) for i in str(n)]
    res1 = sum(i for i in lst if i % 2 == 0)
    return res1


def sumEvenPlace(n):
    lst = [int(i) for i in str(n)]
    res2 = 0
    for i in range(len(lst)):
        if (i + 1) % 2 == 0:
            res2 += lst[i]
    return res2


for n in range(1, 1000):
    if abs(sumEvenNums(n) - sumEvenPlace(n)) == 9:
        print(n)
        break
