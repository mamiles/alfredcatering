#!/usr/bin/env python3

import cgi
import cgitb
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sys.path.insert(0, "/local/sites/alfredcatering.com/htdocs")
from cgi_bin.re_captcha import ReCaptcha
from cgi_bin.HTML import Table

cgitb.enable()
cgitb.enable(display=0, logdir="/local/sites/alfredcatering.com/log")

captcha = ReCaptcha(secret_key='6Lf_2BEUAAAAAFp8AUaJGKjvccufmlXok_Ouu0SL')


def send_mail(mail_text, subject, to, type='plain'):
    from_address = "mamiles@gmail.com"
    comma_space = ', '
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = comma_space.join(to)
    msg.attach(MIMEText(mail_text, type))
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login('mamiles@gmail.com', 'ipnwiudchkkvwhvg')
    server.sendmail(from_address, to, msg.as_string())
    server.quit()
    return

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head><title>alfredcatering.com contact email generation</title></head>')
print('<body>')

form = cgi.FieldStorage()

recaptcha = form.getfirst('g-recaptcha-response', '')
value = captcha.is_success(recaptcha)
if value is False:
    print('<h1>Invalid Captcha.  Please send try again or send email to alfred@alfredcatering.com</h1><br />')
    print('</body>')
    print('</html>')
    sys.exit()

firstName = form.getfirst("firstName", "")
lastName = form.getfirst("lastName", "")

mail_text = """\
<html>
  <head>Customer Contact Info from alfredcatering.com</head>
  <body>
"""
mail_text += 'First Name: %s' % firstName
mail_text += 'Last Name: %s' % lastName

contact_table = Table(header_row=['Attribute', 'Value'])
contact_table.rows.append(['First Name', form.getfirst("firstName", "")])
contact_table.rows.append(['Last Name', form.getfirst("lastName", "")])
mail_text += str(contact_table)

mail_text += """\
        </p>
    </body>
</html>
"""

to_address = 'mamiles@gmail.com'.split()
mail_type = 'html'  # 'html'
send_mail(mail_text, 'Customer Contact', to_address, mail_type)

print('<h1>Hello ' + firstName + ' ' + str(value) + '! Thanks for using my script!</h1><br />')


print('</body>')
print('</html>')

# cgi.test()
