"""
Ада составляет шестибуквенные слова из букв Д, Е, Й, К, С, Т, Р, А.
Буква Й встречается в слове ровно один раз, и после неё обязательно
идёт согласная. Буквы в слове не повторяются. Сколько слов может составить Ада?
"""
from itertools import permutations

count = 0
for i in permutations('ДЕЙКСТРА', r=6):
    lst = ''.join(i)
    if any(item in lst for item in ['ЙД', 'ЙС', 'ЙР', 'ЙК', 'ЙТ']):
        count += 1

print(count)