"""
This is a script to send out an HTML email from Gmail
"""


#!/usr/bin/env python3
import smtplib
import getpass
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)
    email_password = getpass.getpass("Email Password: ")      
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'html'))  # 'html' allows you to send msg in html

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    try:  # To send an email
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Using Gmail's secure server
        smtpObj.ehlo()  # Introduce yourself to Gmail's server
        smtpObj.login(send_from, email_password)
        smtpObj.sendmail(send_from, send_to, msg.as_string())  # Send it
        smtpObj.close()  # Close the session
        print("Successfully sent email to{}".format(send_to))

    except smtplib.SMTPException:  # Except when there is an email error
        print("Error: unable to send email")



# Your Email Address
me = "someone@example.com"

# Their Email Addresses - Currently must be a list
them = ["someoneelse@gmail.com", "another@gmail.com"]

# The subject that you want for your email
subj = "Your Email Subject"

# The Email Text - Can be written in HTML for prettyness' sake
body = "Send a file with this email"

# Get your signature by opening email you sent > Right click on signature > Inspect Element >
# Find div of gmail_signature > Right Click > Copy OuterHTML
signature = '''
some really really really long html path (4000 + characters in my case)
'''

# Any attachments to send, default NONE
attachments = ["myfile.txt", "yourfile.txt"]

# Call the function
# send_mail(me, them, subj, "{} {}".format(body, signature), files=attachments)
