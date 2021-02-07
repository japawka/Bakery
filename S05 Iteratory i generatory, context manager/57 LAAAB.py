import os
import zipfile
import requests
import contextlib

class FileFromWeb:
    def __init__(self, url, temp_file):
        self.url = url
        self.temp_file = temp_file

    def download_file(self):
        r = requests.get(self.url)
        with open(self.temp_file, 'wb') as file:
            file.write(r.content)
            return self

    def close(self):
        #if os.path.isfile(self.temp_file):
        os.remove(self.temp_file)


with contextlib.suppress(FileNotFoundError):
    with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip',
                           r'D:\Python\Python_kurs_sredniozaawansowany\files\euroxref.zip')) as f:
        f.download_file()


        with zipfile.ZipFile(f.temp_file, 'r') as z:
            a_file = z.namelist()[0]
            os.chdir(r'D:\Python\Python_kurs_sredniozaawansowany\files')
            z.extract(a_file, '.', None)
        os.remove(f.temp_file)