import itertools as it
import os

filepath = r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt'

data = []
with open(filepath) as file:
    for line in file:
        elemennts = line.rstrip('\n').split(':')
        d = {'type': elemennts[0], 'action': elemennts[1]}
        data.append(d)

data = sorted(data, key=lambda x: x['type'])
for key, element in it.groupby(data, key=lambda x: x['type']):
    # print(key, list(element))
    print(key, len(list(element)))


################################          LAB              ##########################################################

def scan_tree(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                yield entry
                yield from scan_tree(entry.path)
            else:
                yield entry


listing = scan_tree(r'D:\Python\Python_kurs_sredniozaawansowany\files')

for l in listing:
    print('Katalog: ' if l.is_dir() else 'plik: ', l.path)

listing = scan_tree(r'D:\Python\Python_kurs_sredniozaawansowany\files')

lista = sorted(listing, key=lambda x: x.is_dir())

for key, element in it.groupby(lista, key=lambda x: x.is_dir()):
    print('Katalogów: ' if key else 'plików: ', len(list(element)))
