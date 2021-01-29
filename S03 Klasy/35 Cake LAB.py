
class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
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
        print('--------------------')

    def __str__(self):
        return f'Name {self.name}, taste {self.taste}, additives: {self.additives}'

    def __iadd__(self, other):
        if type(other) is str:
            self.additives.append(other)
            return self

        if type(other) is list:
            self.additives.extend(other)
            return self



cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake_02 = Cake('Chocolate muffin', 'muffin', 'chocolate', ['raisins', 'nuts'], 'cocoa')
cake_03 = Cake('Alaska Snow', 'donut', 'caramel', ['mint'], '')
cake_04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')
for cake in Cake.bakery_offer:
    print(cake)
print()

cake_01 += ['Happy Anniversary', 'From children']
for cake in Cake.bakery_offer:
    print(cake)
