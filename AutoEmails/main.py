import smtplib
from data import *
import time

#verificar o provedor do email para startar servidor#
while True:
    email_type = str(input("What's your e-mail provider?")).lower()

    if email_type == "gmail":
        host = gmail["host"]
        port = gmail["port"]
        break
    elif email_type == "outlook":
        host = outlook["host"]
        port = outlook["port"]
        break
    else:
        print("We don't have support with this e-mail provider")
        time.sleep(1)
        pass

server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()

while True:
    login = str(input(white_text + "Login: "))
    password = str(input("password: "))

    try:
        server.login(login, password)
        print(green_text + "Login successfully")
        break
    except:
        print(red_text + "Login and/or password")
        pass
