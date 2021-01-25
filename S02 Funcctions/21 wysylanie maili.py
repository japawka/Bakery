import smtplib


mailFrom = 'monty Python'
mailTo = ['japawka@poczta.onet.pl', 'kwartet_jalousie@interia.pl']
mailSubject = "Greetings from Python"
mailBody = "Hello from python"

message = f'''From: {mailFrom}
Subject: {mailSubject}

{mailBody}
'''

user = 'agajarzecka@gmail.com'
password = 'A@rtificial001'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent succefully')
except:
    print("ERROR")
