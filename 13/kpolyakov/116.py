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
    last = path[-1]
    if last == target and len(path) > 1:
        count += 1
        print(path)
        return
    for vertex in G[last]:
        if not vertex in path or vertex == target:
            findPath(path + vertex, target)


findPath('Ж', 'Ж')
print(count)
