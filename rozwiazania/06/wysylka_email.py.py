from email.message import EmailMessage
import smtplib

# dane do logowania (testowe konto)
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465                  
MAIL_USER = "testingmagic123456@gmail.com"
MAIL_PASSWORD = "blk....avjuf"

# tworzymy wiadomość
msg = EmailMessage()
msg["Subject"] = "My magical me"
msg["From"] = MAIL_USER
msg["To"] = MAIL_USER # sam do siebie wysyłam maila
msg.set_content("Tak magiczny email, że oczarował nawet mnie!")

# wysyłamy wiadomość
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp_setup:
    smtp_setup.login(MAIL_USER, MAIL_PASSWORD)
    smtp_setup.send_message(msg)

print("✅ Mail wysłany — sprawdź skrzynkę (lub folder Spam).")