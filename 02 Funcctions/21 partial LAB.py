import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"

url = 'http://www.kwartet-jalousie.com/'
dir = r'D:\Python\Python_kurs_sredniozaawansowany\files'
file = 'kwartet.html'
#save_url_file(url, dir, file, msg)

save_url_to_dir = functools.partial(save_url_file, dir=
r'D:\Python\Python_kurs_sredniozaawansowany\files', msg="Please wait: {}")

save_url_to_dir(url = url, file = file)