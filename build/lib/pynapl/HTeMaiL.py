#!/usr/bin/env python3
"""
HTeMaiL.py makes automating emails a simple task.

Three Steps to Email:

    Terminal:

       $ pip(3) install pynapl

    Python3:

        from pynapl import send_mail
        send_mail(me, [them], subj, text, [files], password)

"""

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, text='''
This email was sent via a Python Script, using PYNAPL

          \/
         \||/
         \||/
        <><><>
       <><><><>
       <><><><>
        <><><>

                                          ''', subject="An email from PYNAPL", files=None, server="smtp.gmail.com",
              port="465", password="Email Password"):
    """
    This is a script to send out an HTML email.

    Optionally, you can attach files and send them as well.

    Below is an example email you might send to someone using the HTeMaiL function 'send_mail'

    * Your Email Address          - MANDATORY
    me = "someone@example.com"

    * Their Email Addresses - Must be a list              - MANDATORY
    them = ["someoneelse@gmail.com", "another@gmail.com"]

    * The Email Text - Can be written in HTML for prettyness' sake   - DEFAULT

    '''
    This email was sent via a Python Script, using PYNAPL

              \/
             \||/
             \||/
            <><><>
           <><><><>
           <><><><>
            <><><>

                                              '''


    body = "Send a file with this email"

    * The subject that you want for your email          - DEFAULT "Default Subject"
    subj = "Your Email Subject"

    * Get your signature by opening email you sent > Right click on signature > Inspect Element >
    * Find div of gmail_signature > Right Click > Copy OuterHTML
    signature = '''
    some really really really long html path (4000 + characters in my case)
    '''

    * Any attachments to send, default NONE
    attachments = ["myfile.txt", "yourfile.txt"]

    * Call the function
    send_mail(me, them, "{} {}".format(body, signature), subj, files=attachments)

    """

    assert isinstance(send_to, list)
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
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(f))
        msg.attach(part)

    try:  # To send an email
        smtpObj = smtplib.SMTP_SSL(server, int(port))  # Default to Gmail's secure server
        smtpObj.ehlo()  # Introduce yourself to the email server
        smtpObj.login(send_from, password)
        smtpObj.sendmail(send_from, send_to, msg.as_string())  # Send it
        smtpObj.close()  # Close the session
        print("Successfully sent email to{}".format(send_to))

    except smtplib.SMTPException:  # Except when there is an email error
        print("Error: unable to send email")
