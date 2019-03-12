#!/usr/bin/env python3
import csv      # To read csv data in
import smtplib  # To send an email
import getpass  # To get a password without exposing it to the world


def send_lab_link():
    sent_from = input("Instructor Email: ") # TODO sysargs
    email_password = getpass.getpass(prompt="Email Password: ")
    with open("students.txt") as students:  # Opens the 
        csv_reader = csv.reader(students, delimiter=",")
        student_count = 1
        for x in csv_reader:
            to = [x[1]]
            subject = "Alta3 Lab Access"
            if student_count < 10:
                body = "\n Hello {}, Here is the link to your student lab environment: \n " \
                    "https://labs.alta3.com/?path=test-00{}&password=alta3&autoconnect=true&resize=scale".format(x[0],
                                                                                                        student_count)
            elif student_count < 100:
                body = "\n Hello {}, Here is the link to your student lab environment: \n " \
                       "https://labs.alta3.com/?path=test-0{}&password=alta3&autoconnect=true&resize=scale".format(x[0],
                                                                                                        student_count)
            else:
                body = "\n Hello {}, Here is the link to your student lab environment: \n " \
                       "https://labs.alta3.com/?path=test-{}&password=alta3&autoconnect=true&resize=scale".format(x[0],
                                                                                                        student_count)
            email_text = """
            From: {}
            To: {}
            Subject: {}
            
            {}""".format(sent_from, to, subject, body)
            try:  # To send an email
                smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Using Gmail's secure server
                smtpObj.ehlo()  # Introduce yourself to Gmail's server
                smtpObj.login(sent_from, email_password)
                smtpObj.sendmail(sent_from, to, email_text)  # Send it
                smtpObj.close()  # Close the session
                print("Successfully sent email to{}".format(x[1]))

            except smtplib.SMTPException:  # Except when there is an email error
                print("Error: unable to send email")
            student_count += 1
           
# Call the function
# send_lab_link()



