import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('GMAIL_USER')
EMAIL_PWD = os.environ.get('GMAIL_PWD')

# use for when email multiple people
contacts = ['agarrido84@gmail.com', 'agarrido84@protonmail.com']

msg = EmailMessage()
msg['Subject'] = 'look at these docs'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'agarrido84@protonmail.com'
msg.set_content('send some docs')

# for multiple attachements create a list
files = ['adnetPythonProgammer.docx', 'base2techCover.docx']

# use a for loop to iterate over the multiple attachments
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        # use imghdr when it's an image only attachment
        # file_type = imghdr.what(f.name)
        file_name = f.name

    # for different attachments change the maintype and subtype
    # for images use maintype='image' and subtype='file_type
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PWD)
    smtp.send_message(msg)


