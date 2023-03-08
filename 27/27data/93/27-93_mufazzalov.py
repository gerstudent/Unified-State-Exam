# Автор: Д. Муфаззалов

for file_name in '27-93a.txt', '27-93b.txt':
    f, mm = open(file_name), 10 ** 10
    n, k = map(int, f.readline().split())
    total, ans, left, = 0, -mm, [mm] * k + [0]
    for _ in range(n):
        total += (num := int(f.readline()))
        if num < 0 and num % 10 == 7:
            left.pop(0)
            left.append(total)
        left[k] = min(left[k], total)
        ans = max(ans, total - left[0])
    print(ans)
