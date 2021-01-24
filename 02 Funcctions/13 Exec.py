var_x = 10
password = "My password"
 # eval przjmowało tylko jedną linijkke tekstu
 # exec moze więcej
source = '''
newVar = 1
for i in range(var_x):
    print('-' * i)
    newVar += i
'''
result = exec(source)
print(result)
print(var_x)

print(newVar) # jest na czerwono, bo tej zmiennej nie ma, dopóki program się nie odpali

############################
import os
files_to_process = [
    r"D:\Python\Python_kurs_sredniozaawansowany\math_sin.py",
    r"D:\Python\Python_kurs_sredniozaawansowany\math_sqare.py"
    ]

for file in files_to_process:
    print(os.path.basename(file))
    with open(file, 'r') as file:
        source = file.read()
        exec(source)
# for file_path in files_to_process:
#     with open(file_path, 'r') as f:
#         print("File {} ...".format(os.path.basename(file_path)))
#         source = f.read()
#         exec(source)