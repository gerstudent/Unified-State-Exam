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


def findPath(path, target):
    global count
    lastTown = path[-1]
    if lastTown == target and len(path) > 1:
        count += 1
        print(path)
        return
    for town in G[lastTown]:
        if not town in path or town == target:
            findPath(path + town, target)


findPath('Е', 'Е')
print(count)
