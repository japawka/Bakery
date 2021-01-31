clients = {
    "INFO": 0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER": 0.1,
    "OMEGA": 0.0
}

myClient = input('Enter a client name: ')
total_cost = 7200

try:
    print(f'The % ratio for {myClient} is {clients[myClient]}')
except Exception as e:
    print("No such client",e)
else:  # wykona się tylko wtedy, kiedy nie ma błedu
    print(f'The total cost for {myClient} is {clients[myClient] * total_cost}')
finally: # zawsze się wykona
    print('--- Calculation finished===')

##########################################  LAB

import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo.eu'
dir = r'D:\Python\Python_kurs_sredniozaawansowany\files'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    save_url_to_file(url, tmpfile_path)
    shutil.copyfile(tmpfile_path, file_path)
except Exception as e:
    print("sorry, we have an error", e)
else:
    print("SUCCES")
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print("operation finished")


