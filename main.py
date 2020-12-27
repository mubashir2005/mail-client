import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# config for getting secrets from env
import os
from dotenv import load_dotenv

load_dotenv()
# config ends

# cauz i am using gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.ehlo()


server.login(os.getenv("Email"), os.getenv("Password"))

msg = MIMEMultipart()
msg["From"] = "Mohammed Mubashir Hasan"
msg["To"] = "Mohammed Mubashir Hasan"
msg["Subject"] = "Just a mail client"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

filename = "photo.jpg"

attachment = open(filename,'rb')
p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header("Content-Deposition", f"attachment, filename={filename}")
msg.attach(p)
text = msg.as_string()

server.sendmail(os.getenv("SendEmail"), os.getenv("SendEmail"), text)
