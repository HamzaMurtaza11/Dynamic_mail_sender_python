from importlib.resources import path
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html= Template (path('mail_decorator.html').read_text())

email = EmailMessage()
email['from']='dummy'
email['to']='hamzamurtaza11@gmail.com'
email['subject']='You won 1,000,000 dollars !'

email.set_content(html.subtitute({'name':"Hamza"}),"html")


with smtplib.SMPTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyemail@gmail.com','abc123')
    smtp.send_message(email)
    print("email sent")
