from contextlib import contextmanager


class Door:
    def __init__(self, where):
        self.where = where

    def open(self):
        print(f'Opening door to the {self.where}')

    def close(self):
        print(f'Closing door to the {self.where}')


@contextmanager
def OpenAndClose(obj):
    obj.open()
    yield obj
    obj.close()


with OpenAndClose(Door('next room')) as door:
    print(f'the door is to the {door.where}')

print()


@contextmanager
def OnlyClose(obj):
    yield obj
    obj.close()


with OnlyClose(Door('new room')) as door:
    door.open()
    print(f'the door is to the {door.where}')
#####################################################################################
from urllib.request import urlopen
from contextlib import closing

# with closing(urlopen('http://www.kursyonline24.eu')) as page:
#     for line in page:
#         print(line)

##########################################################

import os
#os.remove(r'D:\Python\Python_kurs_sredniozaawansowany\files\euroxref.zip')  # po drugim wywolaniu błąd, bo =już nie ma pliku

from contextlib import suppress  # z tym juz nie b pokaże błędu
with suppress(FileNotFoundError):
    os.remove(r'D:\Python\Python_kurs_sredniozaawansowany\files\euroxref.zip')

################################################
from contextlib import redirect_stdout   # zapisza komunikat w pliku zamiast wyswietlić na ekranie
f = open(r'D:\Python\Python_kurs_sredniozaawansowany\files\testowy_plik.txt', 'w')
with redirect_stdout(f):
    print('Hello')
    d = Door('EXIT')
    d.open()
    d.close()