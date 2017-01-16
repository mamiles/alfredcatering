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

mail_text = """\
<html>
  <head>Customer Contact Info from alfredcatering.com</head>
  <body>
  <br>
"""

contact_table = Table(header_row=['Attribute', 'Value'])
contact_table.rows.append(['Company Name', form.getfirst("businessName", "")])
contact_table.rows.append(['First Name', form.getfirst("firstName", "")])
contact_table.rows.append(['Last Name', form.getfirst("lastName", "")])
contact_table.rows.append(['Address', form.getfirst("address", "")])
contact_table.rows.append(['City', form.getfirst("city", "")])
contact_table.rows.append(['State', form.getfirst("state", "")])
contact_table.rows.append(['Zip Code', form.getfirst("zip", "")])
contact_table.rows.append(['Phone', form.getfirst("phone", "")])
contact_table.rows.append(['Alt Phone', form.getfirst("altPhone", "")])
contact_table.rows.append(['E-Mail', form.getfirst("email", "")])
contact_table.rows.append(['Alt Email', form.getfirst("altEmail", "")])
contact_table.rows.append(['Type of Event', form.getfirst("eventType", "")])
contact_table.rows.append(['Event Date', form.getfirst("eventDate", "")])
contact_table.rows.append(['Venue Address', form.getfirst("venueAddress", "")])
contact_table.rows.append(['Venue Contact Person', form.getfirst("venuePerson", "")])
contact_table.rows.append(['Event Time', form.getfirst("eventTime", "")])
contact_table.rows.append(['Venue Contact Phone', form.getfirst("venuePhone", "")])
contact_table.rows.append(['Number of Guests', form.getfirst("numberGuests", "")])
contact_table.rows.append(['Menu Preference', form.getfirst("menuPreference", "")])
contact_table.rows.append(['How did you hear about us?', form.getfirst("referral", "")])
contact_table.rows.append(['If other, please specify', form.getfirst("otherReferral", "")])

mail_text += str(contact_table)

mail_text += '<p>Comments:<br>'
mail_text += '<p>%s<br>' % form.getfirst("comments", "")

mail_text += """\
        </p>
    </body>
</html>
"""

to_address = 'mamiles@gmail.com'.split()
mail_type = 'html'  # 'html'
send_mail(mail_text, 'Customer Contact', to_address, mail_type)

#print('<h1>Hello ' + firstName + ' ' + str(value) + '! Thanks for using my script!</h1><br />')


print('</body>')
print('</html>')

# cgi.test()
