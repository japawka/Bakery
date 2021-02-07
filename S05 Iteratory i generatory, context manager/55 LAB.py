import os
import zipfile
import requests

class FileFromWeb:
    def __init__(self, url, temp_file):
        self.url = url
        self.temp_file = temp_file

    def __enter__(self):
        r = requests.get(self.url)
        with open(self.temp_file, 'wb') as file:
            file.write(r.content)
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip',
                       r'D:\Python\Python_kurs_sredniozaawansowany\files\euroxref.zip') as f:
    with zipfile.ZipFile(f.temp_file, 'r') as z:
        a_file = z.namelist()[0]
        os.chdir(r'D:\Python\Python_kurs_sredniozaawansowany\files')
        z.extract(a_file, '.', None)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)