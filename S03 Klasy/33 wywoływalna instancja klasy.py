class MemoryClass:

    def __init__(self, list):
        self.List_of_items = list

    def __call__(self, item):
        self.List_of_items.append(item)

mem = MemoryClass([])

print("List of items in memory:", mem.List_of_items)

mem.List_of_items.append('buy sugar')
print("List of items in memory:", mem.List_of_items)

print(callable(MemoryClass)) # callable
print(callable(mem)) # non collable na razie, zmienimy to metodą __call__

mem('go to walk') # i juz mozna wywołac instancję jako fiunkcję dodającą do swojej listy coś nowego
mem('buy coffe')
print("List of items in memory:", mem.List_of_items)

#################################### Lab
print()
class NoDuplicates:
    def __init__(self):
        self.List_of_items = []

    def __call__(self, new_items):
        for item in new_items:
            if item not in self.List_of_items:
                self.List_of_items.append(item)

my_no_dup_list = NoDuplicates()
print(my_no_dup_list.List_of_items)
my_no_dup_list(['keyboard','mouse'])
my_no_dup_list(['keyboard','mouse', 'monitor'])

print(my_no_dup_list.List_of_items)

