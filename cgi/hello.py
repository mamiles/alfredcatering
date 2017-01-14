#!/usr/bin/env python3

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head><title>My First CGI Program</title></head>')
print('<body>')
print('<p> It works!!! </p>')
for i in range(5):
    print('<h1>Hello World! ' + i + '</h2>')
print('</body>')
print('</html>')
