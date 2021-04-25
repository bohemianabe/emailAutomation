import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('GMAIL_USER')
EMAIL_PWD = os.environ.get('GMAIL_PWD')

# use for when email multiple people
contacts = ['agarrido84@gmail.com', 'agarrido84@protonmail.com']

class followUpEmail:
    def __init__(self, email, subject, coverLetter, resume, date):
        self.email = email
        self.subject = subject
        self.coverLetter = coverLetter
        self.resume = resume
        self.date = date

    def sendEmail(self):
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.email
        msg['BCC'] = "agarrido84@gmail.com"
        msg.set_content("""
        Hi! I just wanted to follow up.
        I applied to your vacant position earlier this month on: {0}, and
        wanted to express my genuine interest in the position, and to speak
        further with you about possibly working together.
        I understand that during this unprecedent time you probably have a lot of
        candidates to consider, and I'm only reaching out again because I'm
        confident that your organization is a great place to work at, and that I
        can bring the talents your web development team is looking for.
        Enjoy the rest of the week, and I hope to hear from you soon.
        Abel Garrido
        Web Developer
        Mobile: 303-999-6683
        https://bohemianabe.github.io/proPage3
        """.format(self.date))
        msg.add_alternative("""\
        <!DOCTYPE html>
        <html lang="en">
          <body style="padding: 5px">
            <h2 style="color: SlateGray; padding-bottom: 5px">
            Hi! &#128075; I just wanted to follow up.
            </h2>
            <p style="color: rgb(32, 32, 32)">
            I applied to your vacant position earlier this month on: {0}, and
            wanted to express my genuine interest in the position, and to speak
            further with you about possibly working together.
            </p>
            <p style="color: rgb(32, 32, 32)">
            I understand that during this unprecedent time you probably have a lot of
            candidates to consider, and I'm only reaching out again because I'm
            confident that your organization is a great place to work at, and that I
            can bring the talents your <b>web development team</b> is looking for.
            </p>
            <p style="color: rgb(32, 32, 32)">
            Enjoy the rest of the week, and I hope to hear from you soon.
            </p>
            <div style="line-height: 0%">
            <p style="color: rgb(32, 32, 32)">Abel Garrido</p>
            <p style="color: rgb(32, 32, 32)">Web Developer</p>
            <p style="color: rgb(32, 32, 32)">mobile: 303-999-6683</p>
            <p style="font-size: smaller">
            <a style="color: darkblue" href="https://bohemianabe.github.io/proPage3"
            >website/portfolio</a
            >
            </p>
            </div>
            <p
            style="
                text-align: right;
                font-size: smaller;
                color: black;
                margin-top: 8px;
                font-style: italic;
            "
            >
            This email was brought to you by the power of Python. Work Smarter.
            </p>
            </body>
            </html>
            """.format(self.date), subtype='html')

        # for multiple attachements create a list
        files = [self.coverLetter, self.resume]

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



# APRIL 30

CALindman = followUpEmail("bdaley@calindman.com", "Staff Accountant Position", "CALindman_CoverLetter.docx", "Accounting_Resume.docx", "04/16")

# CALindman.sendEmail()

######################################################################################################
