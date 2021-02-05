import os

path = r'D:\Python\Python_kurs_sredniozaawansowany\S03 Klasy'
search_string = "Ford"
file_extension = '.py'

for dir_name, subdir, filenames in os.walk(path):  # przechodzi przez wwzystkie dir i subdir
    #print(dir_name, subdir, filenames)
    for filename in filenames:
        if filename.endswith(file_extension):
            full_file_path = os.path.join(dir_name, filename)
            for line in open(full_file_path):
                if search_string in line:
                    print(filename)

# generator do wyszukiwania plików

def generate_files(base_dir, file_extension):
    for dir_name, subdir, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                full_file_path = os.path.join(dir_name, filename)
                yield full_file_path

# generator do przeszukiwania zawartości plików

def grep_files(search_string, files):
    for file in files:
        with open(file) as text:
            if search_string in text.read():
               yield file

files = generate_files(path, file_extension)
for g in grep_files(search_string, files):
    print(g)

