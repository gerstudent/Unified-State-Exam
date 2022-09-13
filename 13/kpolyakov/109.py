G = {
    'А': "БГ",
    'Б': "Д",
    'В': "АБГД",
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
    last = path[-1]
    if last == target and len(path) > 1:
        count += 1
        print(path)
        return
    for vertex in G[last]:
        if not vertex in path or vertex == target:
            findPath(path + vertex, target)


findPath('Е', 'Е')
print(count)
