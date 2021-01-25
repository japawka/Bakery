listA = list(range(6))
listB = list(range(6))


gen = ((a, b) for a in listA for b in listB if a % 2 != 0 and b % 2 == 0)
print(gen)


print(next(gen))
print(next(gen))
print(30 * '-')
for i in gen: # będzie startować od nastepnego elementu
    print(i)
print(30 * '-')
for i in gen: # tu juz nic nie wydusi, bo sie skończył generator (wypisał wszystkie wartości).
    # Trzeba jeszcze raz odpalić generator
    print(i)

gen = ((a, b) for a in listA for b in listB if a % 2 != 0 and b % 2 == 0)
while True:
    try:
        print(next(gen)) # jeśli przekroczy "zakres" generatora - będzie bład. Dlatego try
    except StopIteration:
        print('all values have been generated')
        break

#######################   LAB

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
routesGen = ((start, stop) for start in ports for stop in ports if start < stop)

counter = 0
for route in routesGen:
    counter +=1
    print(route)
print(counter)