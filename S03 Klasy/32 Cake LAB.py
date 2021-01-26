import pickle
import glob
import os
import types

dir = r"D:\Python\Python_kurs_sredniozaawansowany\files"


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cakes_to_html(cls, path):
    template_header = """
<table border=1>"""
    template_data="""
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer="""</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)


def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)


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
        self.path_to_file = os.path.join(dir, self.name + '.bakery')

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

    def save_to_file(self, path):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as file:
            newCake = pickle.load(file)
        cls.bakery_offer.append(newCake)
        return newCake

    @staticmethod
    def get_bakery_files(path):
        print(glob.glob(path + '/*.bakery'))

    @property
    def Text(self):
        return self.__text

    @Text.setter
    def Text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
            print(f"Text has been changed to {new_text}")
        else:
            print(f"Text can be set only for cake {self.name}")


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', True)
cake_02 = Cake('Chocolate muffin', 'muffin', 'chocolate', ['raisins', 'nuts'], 'cocoa', False, "Happy birthday")
cake_03 = Cake('Alaska Snow', 'donut', 'caramel', ['mint'], '', True)
cake_04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False)

cake_02.sel_filling('vanilla crean')
cake_03.add_additives(['cocoa powder', 'coconuts'])

cake_01.Text = "happy anniversary"
cake_02.Text = "happy birthday"
print("-------------------")
print("Today in our offer: ")
print("-------------------")
for cake in Cake.bakery_offer:
    cake.show_info()

print('-' * 100)
cake_02.save_to_file(cake_02.path_to_file)
cake_03.save_to_file(cake_03.path_to_file)
cake_04.save_to_file(cake_04.path_to_file)

Cake.read_from_file(cake_02.path_to_file)
Cake.read_from_file(cake_04.path_to_file)
for cake in Cake.bakery_offer:
    cake.show_info()

Cake.get_bakery_files(dir)
Cake.Export_1_cake_to_html = export_1_cake_to_html
Cake.Export_1_cake_to_html(cake_02, dir + '\cake02.html')
Cake.Export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.Export_all_cakes_to_html(dir + '\cakes_all.html')

for cake in Cake.bakery_offer:
    cake.Export_this_cake_to_html = types.MethodType(export_this_cake_to_html, cake)

for cake in Cake.bakery_offer:
    cake.Export_this_cake_to_html(os.path.join(dir, cake.name.replace(' ', '_') + '.html'))
