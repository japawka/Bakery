dayType = 2

weekend = 1
workday = 2
holiday = 3

print('OK') if dayType == 1 else print('Shit') if dayType == 2 else print('WOW holiday')

#################     LAB

price = 123
bonus = 23
bonus_granted = False

if bonus_granted: price -= bonus
print(price)
rating = 4
print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')

import datetime

today_weekday = datetime.datetime.now().strftime("%w")

if today_weekday == '1':
    print("pranie")
if today_weekday == "2":
    print("prasowanie")
if today_weekday == '0':
    print("dla nas")


