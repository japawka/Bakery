import itertools as it
import operator

data = [1,2,4,5,6,7,8,3,4,2,8,9,77,8]
result = it.filterfalse(lambda x: x<5, data)
for r in result:
    print(r)

print()

result = it.dropwhile(lambda x: x<5, data)
for r in result:
    print(r)

print()
result = it.islice(data, 4 ,8)
for r in result:
    print(r)

spades = ['Hearts', 'Tiles', 'Clovers', 'Pikes']
figures = ['Ace', 'King', 'Queen', 'jack', '10', '9']

cards = it.product(spades, figures) # każdy z każdym
for r in cards:
    print(r)

data2 = [(1,2),(4,5),(6,7),(8,3),(4,2),(8,9),(77,8)]
result = it.starmap(operator.add, data2)
for r in result:
    print(r)

result = it.takewhile(lambda x: x<5, data)
for r in result:
    print(r)