import pandas as pd
import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

clients = pd.read_excel('emails.xlsx')

email_providers = {
        "gmail": {"host": "smtp.gmail.com", "port": 587},
        "outlook": {"host": "smtp.office365.com", "port": 587},
        "yahoo": {"host": "smtp.mail.yahoo.com", "port": 587},
    }

def insert_client_name(text_body, user):
    return text_body.replace("{user}", user)

def send_emails(login, password, subject, text_body):

    #check the email provider to start the server
    host = email_providers[email_provider]["host"]
    port = email_providers[email_provider]["port"]
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()

    #Login to server
    try:
        server.login(login, password)
        print("Login successfully")
        time.sleep(1)
    except Exception as e:
        print(f"Login and/or password{e}")
        time.sleep(1)

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = login

    # Loop to read line per line and send
    for index, client in clients.iterrows():
        email = client["e-mail"]
        user = client["name"]
        counter = None
        error = False

        try:
            msg = MIMEMultipart()
            msg["Subject"] = subject
            msg["From"] = login
            body = insert_client_name(text_body, user)

            msg["To"] = email
            msg.attach(MIMEText(body))
            server.sendmail(msg["From"], msg["To"], msg.as_string())
            print(f"{client["e-mail"]} sent!")
        except Exception as e:
            error = True
            counter =+1
            print(f"Error to send email to {email}: {e}")

        if error != False:
            print(f"{counter} errors ocurred")

    server.quit()

#check the provider, login and text
while True:
    email_provider = str(input("E-mail provider: "))
    if email_provider not in email_providers:
        print(f"Unsupported email provider: {email_provider}")
        pass

    else:
        break

login = str(input("login: "))
password = str(input("password: "))

while True:
    print("*use {user} to insert the client name*")
    subject = str(input("Type your subject: "))
    text_body = str(input("Body: "))

    print(f'''Subject: {subject}
{text_body}''')

    confirmation = str(input("Do you want to send this message?(Y/N)").upper())

    match confirmation:
        case "Y":
            send_emails(login, password, subject, text_body)
            break

        case "N":
            print("Returning...")
            time.sleep(1)
            pass

        case _:
            print('Only "Y" or "N"! Returning...')
            time.sleep(1)
            pass