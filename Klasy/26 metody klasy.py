class Car:
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk

    def is_damaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def get_info(self):
        print(f"{self.brand.upper()} {self.model.upper()}")
        print(f"Air bag     -   ok  -   {self.isAirBagOk}")
        print(f"Painting    -   ok  -   {self.isPaintingOk}")
        print(f"Mechanic    -   ok  -   {self.isMechanicOk}")
        print('---------------------------')


car01 = Car("Seat", "Ibiza", True, True, True)
car02 = Car("Ford", "Fiesta", True, False, True)

car01.get_info()
car02.get_info()


################################   LAB

class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

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

    def sel_filling(self, new_filling):
        self.filling = new_filling

    def add_additives(self, new_additives):
        self.additives.extend(new_additives)


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake_02 = Cake('Chocolate muffin', 'muffin', 'chocolate', ['raisins', 'nuts'], 'cocoa')
cake_03 = Cake('Alaska Snow', 'donut', 'caramel', ['mint'], '')
bakeryOffer = [cake_01, cake_02, cake_03]

cake_02.sel_filling('vanilla crean')
cake_03.add_additives(['cocoa powder', 'coconuts'])

print("Today in our offer: ")
print()
for cake in bakeryOffer:
    cake.show_info()

# print("Today in our offer: ")
# for cake in bakeryOffer:
#     print(
#         f'{cake.name} - ({cake.kind}), main taste: {cake.taste} with additive of {cake.additives}, filled with {cake.filling}')
