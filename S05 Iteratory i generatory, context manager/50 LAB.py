import os
import requests

def gen_get_files(dir):
    files = os.listdir(dir)
    for file in files:
        full_path = os.path.join(dir, file)
        yield full_path

def gen_get_file_lines(filename):
    with open(filename) as file:
        for line in file:
            yield line.rstrip('\n')

def check_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return True
    except:
        return False


path = r'D:\Python\Python_kurs_sredniozaawansowany\files\url'

for f in gen_get_files(path):
    for line in gen_get_file_lines(f):
        print(f'{f} - {line} - {check_url(line)}')

