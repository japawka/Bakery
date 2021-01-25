listA = list(range(1,6))
listB = list(range(1, 6))

for a in listA:
    row = ''
    for b in listB:
        row += f'{a * b:4}'
    print(row)

product = []
for a in listA:
    for b in listB:
        product.append((a, b))
print(product)

prduct2 = [(a, b) for a in listA if a % 2 == 0 for b in listB if b % 2 != 0] # kod ponizej to samo daje
prduct3 = [(a, b) for a in listA for b in listB if a % 2 != 0 and b % 2 == 0]
prductComp = [(a, b) for a, b in zip(listA, listB)]
print(prduct2)
print(prduct3)

prductDict = {a: b for a in listA for b in listB }
print(prductDict)

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [(start, stop) for start in ports for stop in ports]
routes = [(start, stop) for start in ports for stop in ports if start != stop]
routes = [(start, stop) for start in ports for stop in ports if start < stop]
#routes = [(start, stop) for start in ports for stop in ports if ports.index(start) < ports.index(stop)]

counter = 1
for route in routes:
    print(counter, route)
    counter +=1