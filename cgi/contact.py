#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

firstName = form.getfirst("firstName", "").upper()

print('<h1>Hello ' + firstName + '! Thanks for using my script!</h1><br />')


