import os

print()
print("current directory is:", os.getcwd())
currentDir = os.getcwd()
filename = "result.txt"
fullPath = os.path.join(currentDir, filename)
print('the constructed file path is', fullPath)

path = r'D:\Python\Python_kurs_sredniozaawansowany\files\data02.txt'
# os.remove(path)

if os.path.isfile(path):
    print(f'File {path} exists')
else:
    print(f"creating file {path}")
    open(path, 'x').close()
    print(f'File {path} is created')

# to poniżej zastępuje to powyżej

result = os.path.isfile(path) or open(path, 'x').close()  # jeśli perwszy warunek jest prawdziwy,
# to Python drugiego juz nie sprawdza. jesli perwszy jest False, wtedy sprawdza drugi, a w tym
# przypadku jest zwracane None
print(result)


#################################  LAB
#path = r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt'
def count_words(file):
    with open(file, 'r') as source:
        r = source.read().split()
        return len(r)

if os.path.isfile(path):
    print(count_words(path))

os.path.isfile(path) and print(count_words(path))