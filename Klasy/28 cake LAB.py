class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    def __init__(self, name, kind, taste, additives, filling, gluten_free = False):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(f'{self.name.upper()} ({self.kind})')
        print(f'Taste:     {self.taste} ')
        if self.additives:
            print('Additives: ')
            for a in self.additives:
                print(f'\t {a}')
        if self.filling:
            print(f'Filling:    {self.filling}')
        print(f'Gluten free:    {self.__gluten_free}')
        print('--------------------')

    def sel_filling(self, new_filling):
        self.filling = new_filling

    def add_additives(self, new_additives):
        self.additives.extend(new_additives)


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', True)
cake_02 = Cake('Chocolate muffin', 'muffin', 'chocolate', ['raisins', 'nuts'], 'cocoa')
cake_03 = Cake('Alaska Snow', 'donut', 'caramel', ['mint'], '', True)
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')


cake_02.sel_filling('vanilla crean')
cake_03.add_additives(['cocoa powder', 'coconuts'])

print("Today in our offer: ")
for cake in cake_01.bakery_offer:
    cake.show_info()

cake_01.__gluten_free = False
print(vars(cake_01))

cake_01._Cake__gluten_free = False
cake_01.show_info()
