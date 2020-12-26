import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com ", 465)

server.ehlo()

with open("password.txt", "r") as f:
    password = f.read()

server.login("mubashirhasan716@gmail.com", password)

msg = MIMEMultipart()
msg["From"] = "mubashirhasan716@gmail.com"
msg["To"] = "mubashirhasan2005@outlook.com"
msg["Subject"] = "Just a mail client"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

filename = "photo.jpg"

attachment = open(filename, "rb")

p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header("Content-Deposition", 'filename')
text = msg.as_string()

server.sendmail("mubashirhasan716@gmail.com", "mubashirhasan2005@outlook.com", text)
