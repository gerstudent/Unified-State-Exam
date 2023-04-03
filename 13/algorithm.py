# 6748 kompege

G = {
    'А': "БГ",
    'Б': "Д",
    'В': "АБГДЖ",
    'Г': "Ж",
    'Д': "ЕИ",
    'Е': "ВКЛ",
    'Ж': "Е",
    'И': "ЕЛ",
    'К': "Ж",
    'Л': "К",
}

count = 0


def findPath(path, target):
    global count
    lastTown = path[-1]
    # Если дошли до конечного пункта, то увеличиваем счётчик и выводим построенный путь на экран:
    if lastTown == target and len(path) > 1:
        count += 1
        print(path)
        return

    for town in G[lastTown]:
        # если новой вершины еще нет в пройденном маршруте или она совпадает с конечной точкой.
        if not town in path or town == target:
            findPath(path + town, target)


findPath('Е', 'Е')
print(count)
