#!/usr/bin/env python3
import cgi
import cgitb
import os

cgitb.enable()

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head><title>My First CGI Program</title></head>')
print('<body>')

form = cgi.FieldStorage()

firstName = form.getfirst("firstName", "")
lastName = form.getfirst("lastName", "")

print('<h1>Hello ' + firstName + ' ' + lastName + '! Thanks for using my script!</h1><br />')


print('</body>')
print('</html>')

cgi.test()
