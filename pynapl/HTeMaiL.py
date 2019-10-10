#!/usr/bin/env python3
"""
HTeMaiL.py makes automating emails a simple task.

Three Steps to Email:

    Terminal:

       $ pip(3) install pynapl

    Python3:

        from pynapl import send_mail
        send_mail(send_from, send_to, subj=, text=, files=, password=, server=, port=)

See the send_mail() function for details

This project requires dependencies only from the Python Standard Library
"""

from getpass import getpass
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, text='This email was sent via a Python Script, using PYNAPL',
              subject="An email from PYNAPL", files=None, server="smtp.gmail.com",
              port="465", password=getpass()):

    """Allows you to send emails


    :param send_from: Mandatory - Your Email Address            - str
    :param send_to:   Mandatory - Their Email Address           - str OR list of str
    :param subj:      Optional  - Subject of Email              - str
    :param text:      Optional  - Body/Text of the Email        - str
    :param files:     Optional  - Files to be Attached to Email - str OR list of str
    :param password   Optional  - Password for your email       - str OR be prompted in Terminal
    :param server     Optional  - Email Server Address          - str
    :param port       Optional  - Port for Email Server         - str

    """

    try:
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        if isinstance(send_to, list):
            msg['To'] = COMMASPACE.join(send_to)
        else:
            msg['To'] = send_to

        msg.attach(MIMEText(text, 'html'))  # 'html' allows you to send msg in html
    except TypeError:
        print("You need to verify that your 'send_from', 'send_to', and 'subject' are the right type")

    try:
        if isinstance(files, list):
            for f in files or []:
                with open(f, "rb") as fil:
                    part = MIMEApplication(fil.read(), Name=basename(f))
                # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(f))
                msg.attach(part)
        else:
            with open(files, "rb") as fil:
                part = MIMEApplication(fil.read(), Name=basename(files))
            part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(files))
            msg.attach(part)
        print('Sending Email with Attached Files | {} | to | {} |'.format(files, send_to))
    except TypeError:
        print('Sending Email with No Files Attached to | {} |'.format(send_to))

    try:  # To send an email
        smtp_obj = smtplib.SMTP_SSL(server, int(port))  # Default to Gmail's secure server
        smtp_obj.ehlo()  # Introduce yourself to the email server - Handshake
        smtp_obj.login(send_from, password) # Login
        smtp_obj.sendmail(send_from, send_to, msg.as_string())  # Send it
        smtp_obj.close()  # Close the session
        print("Successfully sent email to {}".format(send_to))

    except smtplib.SMTPException:  # Except when there is an email error
        print("Error: unable to send email to {}".format(send_to))
