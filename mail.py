import smtplib
import imghdr
from email.message import EmailMessage

def sendEmail(image):
    fromEmail = 'alexarnimueller@gmail.com'
    fromEmailPassword = 'xublapmotrygawmj'
    toEmail = 'arnimueller.alex@bluewin.ch'
        
    msg = EmailMessage()
    msg['Subject'] = 'Security Camera Update'
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg.preamble = 'Raspberry pi security camera update'
    msg.add_attachment(image, maintype='image', subtype=imghdr.what(None, image))
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, fromEmailPassword)
    smtp.send_message(msg)
    smtp.quit()
