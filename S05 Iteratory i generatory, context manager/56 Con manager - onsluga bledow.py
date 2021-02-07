import os


class Ini_file:
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

    def __exit__(self, exc_type, exc_val, exc_tb):  # ta metoda obsługuje błedy,
        # jeśli chcemy je ukryć to ttrzeba zwrócić True,
        # jeśli chcemy je pokazać na zewnątrz - trzeba zwrócić False
        print(f'exc type: {exc_type}')
        print(f'exc val: {exc_val}')
        print(f'exc tb: {exc_tb}')
        if exc_type == OSError:
            return False
        else:
            return True





with Ini_file(r'D:\Python\Python_kurs_sredniozaawansowany\files\my.ini') as ini:
    ini.write_parameter('logging', 'light')
    ini.write_parameter('mode', 'strict')
    ini.save_on_disk()
