G = {
    'А': "Б",
    'Б': "ВЗ",
    'В': "Г",
    'Г': "ДЖЗ",
    'Д': "АЕЖ",
    'Е': "АИ",
    'Ж': "АЗ",
    'З': "АВ",
    'И': "А",
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


findPath('Ж', 'Ж')
print(count)
