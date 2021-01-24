import smtplib
import functools

def send_mail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = f'''From: {mailFrom}
Subject: {mailSubject}
{mailBody}
'''

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent succefully')
        return True
    except:
        print("ERROR")
        return False


user = 'agajarzecka@gmail.com'
password = 'A@rtificial001'
mailFrom = 'monty Python'
mailTo = ['japawka@poczta.onet.pl', 'kwartet_jalousie@interia.pl']
mailSubject = "Greetings from Python by function"
mailBody = "Hello from python"
send_info_email_from_gmail = functools.partial(send_mail, user, password, mailSubject = "Alert") # funkcja
# ta przejmuje część parametrów z innej funkcji, która jest pierwszym parametrem.
# Jeśli chcemy dodac parametr nie w kolejności , to trzeba przez  wartość, ale także w wywołaniu, bo będzie błąd

#send_mail(user, password, mailFrom, mailTo, mailSubject, mailBody)
 # nie musimy juz wpisywać user i password :
send_info_email_from_gmail(mailFrom = mailFrom, mailTo = mailTo, mailBody =  mailBody)