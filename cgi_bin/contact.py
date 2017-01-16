#!/usr/bin/env python3

import cgi
import cgitb
import sys
import os
# sys.path.insert(0, "/local/sites/alfredcatering.com/htdocs/cgi_bin")
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from cgi_bin.re_captcha import ReCaptcha


cgitb.enable()
cgitb.enable(display=0, logdir="/local/sites/alfredcatering.com/log/cgi.log")

captcha = ReCaptcha(secret_key='6Lf_2BEUAAAAAFp8AUaJGKjvccufmlXok_Ouu0SL')

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head><title>My First CGI Program</title></head>')
print('<body>')

form = cgi.FieldStorage()

firstName = form.getfirst("firstName", "")
lastName = form.getfirst("lastName", "")
recaptcha = form.getfirst('g-recaptcha-response', '')
value = captcha.is_success(recaptcha)

print('<h1>Hello ' + firstName + ' ' + value + '! Thanks for using my script!</h1><br />')


print('</body>')
print('</html>')

# cgi.test()