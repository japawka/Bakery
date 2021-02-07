import os


class ini_file:
    def __init__(self, path):
        self.path = path
        self.paramerters = {}
        self.read_from_disk()

    def read_from_disk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    parts = line.replace('\n', '').split('=')
                    self.paramerters[parts[0]] = parts[1]

    def read_paramerters(self, key):
        if key in self.paramerters.keys():
            return self.paramerters[key]
        else:
            return None

    def write_parameter(self, key, value):
        self.paramerters[key] = value

    def save_on_disk(self):
        with open(self.path, 'w') as file:
            for key, value in self.paramerters.items():
                line = f'{key}={value}\n'
                file.writelines(line)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

ini = ini_file(r'D:\Python\Python_kurs_sredniozaawansowany\files\my.ini')
ini.write_parameter('version', 1)
ini.write_parameter('level', 'advance')
ini.save_on_disk()

ini2 = ini_file(r'D:\Python\Python_kurs_sredniozaawansowany\files\my.ini')
print(ini2.paramerters)
print(ini2.read_paramerters('version'))
print(ini2.read_paramerters('level'))

with ini_file(r'D:\Python\Python_kurs_sredniozaawansowany\files\my.ini') as ini3:
    print(ini3.paramerters)
    print(ini3.read_paramerters('version'))
    print(ini3.read_paramerters('level'))