
file = open(r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt')
data = file.read()  # słabe, bo wczytuje całą zawartość pliku do pamięci, a moze być wielki
file.close()

for line in data.splitlines():
    if line.startswith('ACTION'):
        print(line)

        ###############################  inna wersja
print('----------------------------')
file = open(r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt')
for line in file:  # tu wczytujemy po linijce
    if line.startswith('ACTION'):
        print(line.replace('\n', ''))
file.close()

###############################  inna wersja
print('----------------------------')
file = open(r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt')
records = []
for line in file:
    if ':' in line:
        typ, action = line.rstrip('\n').split(':', 1)
        record = (typ, action)
        records.append(record)  # też cała zawartość pliku w pamięci
file.close()
print(records)
###############################  wersja z generatorem
print('----------------------------')

def get_records(file_path):
    print('---opening file---')
    file = open(file_path)

    for line in file:
        if ':' in line:
            typ, action = line.rstrip('\n').split(':', 1)
            record = (typ, action)
            yield record

    print('---closing file---')
    file.close()

fpath = r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt'

for d in get_records(fpath):
    print(f'Type is {d[0]}, and the action is {d[1]}')
