atuple = (1, 2, 3, 4, 5)

for i in atuple:  # mozemy dla iterable uzyć for, ale nie next, bo nie jest iteratorem
    print(i)
print()
btuple = iter(atuple) # po użyciu funkcji iter już jest iteratorem
print(next(btuple))
print(next(btuple))
print(next(btuple))
print(next(btuple))
print()
alist = [1, 2, 3, 4, 5]
# to samo dla listy i setu

with open(r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt', 'r') as file:
    for line in file:
        print(line)
# ale obiekt tworzony do pracy z plikiem jest iteratorem
with open(r'D:\Python\Python_kurs_sredniozaawansowany\files\data.txt', 'r') as file:
    while True:
        try:
            print(next(file))
        except StopIteration:
            break
###################################### ######################  ###########################   ############  LAB
import csv

with open(r'D:\Python\Python_kurs_sredniozaawansowany\files\data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break

