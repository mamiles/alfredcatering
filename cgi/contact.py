#!/usr/bin/env python3

import cgi
import cgitb
from reCaptcha import ReCaptcha

cgitb.enable()
cgitb.enable(display=0, logdir="/local/sites/alfredcatering.com/log/cgi.log")

captcha = reCaptcha(secretKey='6Lf_2BEUAAAAAFp8AUaJGKjvccufmlXok_Ouu0SL')

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head><title>My First CGI Program</title></head>')
print('<body>')

form = cgi.FieldStorage()

firstName = form.getfirst("firstName", "")
lastName = form.getfirst("lastName", "")
recaptcha = form.getfirst('g-recaptcha-response', '')
value = captcha.is_succes(recaptcha)

print('<h1>Hello ' + firstName + ' ' + value + '! Thanks for using my script!</h1><br />')


print('</body>')
print('</html>')

# cgi.test()
