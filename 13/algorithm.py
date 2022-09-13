# Задача: №110 (kpolyakov)

G = {
    'А': "БГ",
    'Б': "ДЕ",
    'В': "АБГ",
    'Г': "ЕЖ",
    'Д': "ЕИЛ",
    'Е': "ВЛ",
    'Ж': "Е",
    'И': "Л",
    'К': "Ж",
    'Л': "ЖК"
}
count = 0


def findPath(path, target):  # path - построенный путь, target - конечный пункт
    global count
    last = path[-1]
    # Если дошли до конечного пункта, то увеличиваем счётчик и выводим построенный путь на экран:
    if last == target and len(path) > 1:
        count += 1
        print(path)
        return
    for vertex in G[last]:
        # если новой вершины еще нет в пройденном маршруте или она совпадает с конечной точкой.
        if not vertex in path or vertex == target:
            findPath(path + vertex, target)


findPath('Е', 'Е')
print(count)
