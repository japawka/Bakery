# clients = {
#     "INFO": 0.5,
#     "DATA": 0.2,
#     "SOFT": 0.2,
#     "INTER": 0.1,
#     "OMEGA": 0.0
# }
#
# myClient = input('Enter a client name: ')
# total_cost = 7200
#
# try:
#     ratio = float(input("Enter new ratio: "))
#     print(f'The default % ratio for {myClient} is {clients[myClient]}, a new one is {ratio}')
#     print(f'The total cost for {myClient} is {ratio * total_cost}')
#     print(f'The new ratio in comparison with old ratio: {clients[myClient] / ratio:.2f}')
# except KeyError as e:
#     print(f"No such client {e} on the list {[a for a in clients.keys()]}")
# except (ValueError, ZeroDivisionError) as v:
#     print('The new ratio has a incorrect value \n Details:', v)
# # except ZeroDivisionError as o:
# #     print('Error', o)
# except Exception as e:
#     print('Sorry, we have an error', e)
#
#
# print('--- Calculation finished===')

#################################### LAB
import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.por-tal.pl/news.php'
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
    os.remove(tmpfile_path)

except requests.exceptions.ConnectionError as e:
    print("Cannot established connection to site", e)
except PermissionError as e:
    print('Cannot write to file', e)
except FileNotFoundError as e:
    print("Cant find file", tmpfile_path)
except Exception as e:
    print("sorry, we have an error", e)
else:
    print("SUCCES")
finally:
    print("operation finished")