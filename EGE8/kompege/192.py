"""
    Иван составляет 5-буквенные слова из букв А, Б, В, Г, Д, Я.
    В каждом слове содержится ровно три буквы Я. Сколько различных
    кодовых слов может составить Иван?
"""
from itertools import product

count = 0
for i in product('АБВГДЯ', repeat=5):
    lst = ''.join(i)
    if lst.count('Я') == 3:
        count += 1

print(count)
