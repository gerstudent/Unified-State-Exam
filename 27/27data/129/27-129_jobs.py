from time import time

# алгоритм без оптимизаций
def enum_simple(filename):
    with open(filename) as f:
        n = int(f.readline())
        nums = [int(f.readline()) for _ in range(n)]*2

    # инициализируем максимальную сумму
    max_s = 0
    # перебиаем индексы начала подпоследовательностей
    for i in range(n):
        # перебираем индексы окончаний подпоследовательностей длины 13
        for fn in range(i+13, i+n, 13):
            # находим сумму элементов подпоследовательности
            s = sum(nums[i: fn])
            # если сумма кратна 13
            if s % 13 == 0:
                # выбираем максимальную
                max_s = max(max_s, s)
    return max_s

# оптимизация набора суммы
def enum_slice(filename):
    with open(filename) as f:
        n = int(f.readline())
        nums = [int(f.readline()) for _ in range(n)]*2

    # инициализируем максимальную сумму
    max_s = 0
    # перебиаем индексы начала подпоследовательностей
    for i in range(n):
        # накапливаем новую сумму
        s = 0
        # перебираем индексы окончаний подпоследовательностей длины 13
        for fn in range(i+13, i+n, 13):
            # добавляем только новые 13 элементов
            s += sum(nums[fn-13: fn])
            # если сумма кратна 13
            if s % 13 == 0:
                # выбираем максимальную
                max_s = max(max_s, s)
    return max_s

# алгоритм с неоптимизированным перебором префиксных сумм
def enum_pref(filename):
    with open(filename) as f:
        n = int(f.readline())
        nums = [int(f.readline()) for _ in range(n)]*2

    pref = [0]*(2*n + 1)
    for i in range(2*n):
        pref[i+1] = pref[i] + nums[i]

    max_s = 0
    # перебиаем индексы начала подпоследовательностей
    for i in range(n):
        # перебираем индексы окончаний подпоследовательностей длины 13
        for fn in range(i+13, i+n, 13):
            # если сумма кратна 13
            if (pref[fn] - pref[i]) % 13 == 0:
                # выбираем максимальную
                max_s = max(max_s, pref[fn] - pref[i])
        
    return max_s


# алгоритм с оптимизированным перебором префиксных сумм
def enum_back(filename):
    with open(filename) as f:
        n = int(f.readline())
        nums = [int(f.readline()) for _ in range(n)]*2

    pref = [0]*(2*n + 1)
    for i in range(2*n):
        pref[i+1] = pref[i] + nums[i]

    max_s = 0
    # перебиаем индексы начала подпоследовательностей
    for i in range(n):
        # перебираем индексы окончаний подпоследовательностей длины 13
        # начинаем с большей длины
        for fn in range(i+n-n%13, i+12, -13):
            # если сумма кратна 13
            if (pref[fn] - pref[i]) % 13 == 0:
                # выбираем максимальную
                max_s = max(max_s, pref[fn] - pref[i])
                # если нашли сумму кратную 13,
                # смысла перебирать дальше нет, сумма будет меньше
                break
    return max_s





for fn in enum_back, enum_pref:
    st = time()  
    print(fn('27C.txt'))
    print(time() - st)
    print('____')



 
