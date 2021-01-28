import random

class MemoryClass:
    list_of_already_selected_items = []

    def __init__(self, func):
        #print("This is init of MemoryClass")
        self.func = func

    def __call__(self, list):
        #print("This is call of MemoryClass instance")
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_items]
       # print('-----> selecting only from list of', items_not_selected)
        item = self.func(items_not_selected)
        MemoryClass.list_of_already_selected_items.append(item)
        #print(MemoryClass.list_of_already_selected_items)
        return item

cars = ["opel", 'Toyota', 'Fiat', 'Mercedes', 'Pontiac', 'BMW', 'Ferrari', 'Audi', 'Mazda']

@MemoryClass
def select_today_promorion(list_od_cars):
    return random.choice(list_od_cars)

@MemoryClass
def select_today_show(list_od_cars):
    return random.choice(list_od_cars)

@MemoryClass
def select_free_accesories(list_od_cars):
    return random.choice(list_od_cars)


print('Promotion: ', select_today_promorion(cars))
print('Show ', select_today_show(cars))
print('Free accesories', select_free_accesories(cars))
