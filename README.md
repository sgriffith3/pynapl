# pynapl

**Python Native Automation Package Library**

The Tastiest Code You May Ever Consume 

## Overview
**pynapl** is the conglomeration of useful tactics that I have made work for my personal and professional automation. The hope is for **pynapl** to evolve and become something more (someday - Exeggutor!!!). 


## Details
**pynapl.send_mail()**

This is a script to send out an HTML email.

`pynapl.send_mail(send_from, send_to, text='''
This email was sent via a Python Script, using PYNAPL`

       \/
      \||/
      \||/
     <><><>
    <><><><>
    <><><><>
     <><><>

`''', subject="An email from PYNAPL", files=None, server="smtp.gmail.com", port="465", password="Email Password")`
    

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

body = "Send a file with this email"

* The subject that you want for your email          - DEFAULT "Default Subject"
subj = "Your Email Subject"

    0. Get your signature by opening email you sent > Right click on signature > Inspect Element >
    0. Find div of gmail_signature > Right Click > Copy OuterHTML
signature = '''
some really really really long html path (4000 + characters in my case)
'''

* Any attachments to send, default NONE
attachments = ["myfile.txt", "yourfile.txt"]

* Call the function
send_mail(me, them, "{} {}".format(body, signature), subj, files=attachments)


## NEVER TESTED ON REAL FRUIT
No warranties. No guarantees. But feel free to enjoy as you please. 

### License

**pynapl** is registered under the MIT license - That means if you use it, mention me and we're cool.
