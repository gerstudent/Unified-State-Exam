'''
Дан файл, состоящий из N чисел, каждое из которых >= 0.
Рассматриваются всевозможные пары различных ненулевых элементов
последовательности, количество нулей между которыми кратно K.
Необходимо найти количество таких пар, с суммой элементов, кратной D.
На вход подаётся три числа: N, K и D. Следом N чисел.
Пример входных данных (для примера N = 8, K = 2, D = 2):
8 2 2
5
0
3
0
0
0
1
9
Ответ для примера: 3.
Пояснение для примера: взяли пары (5;1), (5;9), (1;9).
Между этими парами чётное количество нулей, сумма каждой из них тоже чётна.
'''

F = open('27-118a.txt')
N, K, D = map(int, F.readline().split())
A = [int(x) for x in F]
count = 0
for i in range(N - 1):
    k0 = 0
    if A[i] == 0:
        k0 += 1
    for j in range(i + 1, N):
        if A[j] == 0:
            k0 += 1
        if k0%K == 0:
            if (A[i]+A[j])%D == 0 and A[i] > 0 and A[j] > 0:
                count += 1
print(count)

F = open('27-118b.txt')
N, K, D = map(int, F.readline().split())
count_of_zero = 0
r = [[0]*D for j in range(K)]
count = 0
for i in range(N):
    x = int(F.readline())
    if x == 0:
        count_of_zero += 1
    else:
        count += r[count_of_zero%K][(D - x%D)%D]
        r[count_of_zero%K][x%D] += 1
print(count)
F.close()

