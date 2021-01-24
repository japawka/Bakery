class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text=None):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
        if self.kind == "cake" or text == '':
            self.__text = text
        else:
            self.__text = ''
            print(f"Text can be set only for cake {name}")

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
        if self.__text:
            print(f'Text:    {self.__text}')
        print('--------------------')

    def sel_filling(self, new_filling):
        self.filling = new_filling

    def add_additives(self, new_additives):
        self.additives.extend(new_additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
            print(f"TYext has been changed to {new_text}")
        else:
            print(f"Text can be set only for cake {self.name}")

    Text = property(__get_text, __set_text, None, "Changing or displaying text on cake")


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', True)
cake_02 = Cake('Chocolate muffin', 'muffin', 'chocolate', ['raisins', 'nuts'], 'cocoa', False, "happy birthday")
cake_03 = Cake('Alaska Snow', 'donut', 'caramel', ['mint'], '', True)
cake_04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False)

cake_02.sel_filling('vanilla crean')
cake_03.add_additives(['cocoa powder', 'coconuts'])

print("Today in our offer: ")
for cake in cake_01.bakery_offer:
    cake.show_info()
print()
cake_01.Text = "happy anniversary"
cake_02.Text = "happy birthday"

for cake in cake_01.bakery_offer:
    cake.show_info()

print(cake_01.Text)
