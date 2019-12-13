#!/usr/bin/python3
import cgi, cgitb
form = cgi.FieldStorage()
y = int(form.getvalue('Year'))
formatmethod = form.getvalue("formatmethod")

#Code to calculate Easter Date
a=y%19
b=y//100
c=y%100
d=b//4
e=b%4
g=(8*b+13)//25
h=(19*a+b-d-g+15)%30
j=c//4
k=c%4
m=(a+11*h)//319
r=(2*e+2*j-k-h+m+32)%7
n=(h-m+r+90)//25
p=(h-m+r+n+19)%32

#Code to calculate the Month
if n == 3:
    month = "March"
    x = "03"
elif n == 4:
    month = "April"
    x = "04"
else:
    month == "May"
    x = "05"

#Code to get the right format
if p < 10:
    day = (f"0{p}")
else:
    day = p

#Code to make the program robust if invalid input
if y < 0:
    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
    print('<head> <title> Easter Date </title> </head>')
    print('<body>')
    print(f'<p2>Invalid date <br> </p2>')
    print(f'<p4> Please go back to the <a href="../Form.html">Form</a> and input a valid date </p4>')
    print('</body>')
    print('</html>')


#Code to calculate Easter Date numerically
elif formatmethod == "numerically":

    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
    print('<head> <title> Easter Date </title> </head>')
    print('<body>')
    print(f'<p2>The Easter date of the year {y} is, <br> </p2>')
    print(f'<p4> {day}/{x}/{y} </p4>')
    print('</body>')
    print('</html>')

#Code to calculate Easter Date verbosely
elif formatmethod == "verbosely":
    if p == 1 or p == 21 or p == 31:
        print('Content-Type: text/html; charset=utf-8')
        print('')
        print('<!DOCTYPE html>')
        print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
        print('<head> <title> Easter Date </title> </head>')
        print('<body>')
        print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
        print(f'<p3> {p}<sup>st</sup> of {month} {y} <br> </p3>')
        print('</body>')
        print('</html>')

#Code to calculate the correct superscript
    elif p == 2 or p == 22:
        print('Content-Type: text/html; charset=utf-8')
        print('')
        print('<!DOCTYPE html>')
        print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
        print('<head> <title> Easter Date </title> </head>')
        print('<body>')
        print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
        print(f'<p3> {p}<sup>nd</sup> of {month} {y} <br> </p3>')
        print('</body>')
        print('</html>')

    elif p == 3 or p == 23:
        print('Content-Type: text/html; charset=utf-8')
        print('')
        print('<!DOCTYPE html>')
        print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
        print('<head> <title> Easter Date </title> </head>')
        print('<body>')
        print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
        print(f'<p3> {p}<sup>rd</sup> of {month} {y} <br> </p3>')
        print('</body>')
        print('</html>')

    else:
            print('Content-Type: text/html; charset=utf-8')
            print('')
            print('<!DOCTYPE html>')
            print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
            print('<head> <title> Easter Date </title> </head>')
            print('<body>')
            print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
            print(f'<p3> {p}<sup>th</sup> of {month} {y} <br> </p3>')
            print('</body>')
            print('</html>')

#Code to calculate both format methods
else:
    #Code to calculate the correct superscript
    if p == 1 or p == 21 or p == 31:
        print('Content-Type: text/html; charset=utf-8')
        print('')
        print('<!DOCTYPE html>')
        print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
        print('<head> <title> Easter Date </title> </head>')
        print('<body>')
        print('<br><br><br><br><br><br>')
        print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
        print(f'<p3> {p}<sup>st</sup> of {month} {y} <br> </p3>')
        print(f'<p4> {day}/{x}/{y} </p4>')
        print('</body>')
        print('</html>')

    elif p == 2 or p == 22:
        print('Content-Type: text/html; charset=utf-8')
        print('')
        print('<!DOCTYPE html>')
        print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
        print('<head> <title> Easter Date </title> </head>')
        print('<body>')
        print('<br><br><br><br><br><br>')
        print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
        print(f'<p3> {p}<sup>nd</sup> of {month} {y} <br> </p3>')
        print(f'<p4> {day}/{x}/{y} </p4>')
        print('</body>')
        print('</html>')

    elif p == 3 or p == 23:
        print('Content-Type: text/html; charset=utf-8')
        print('')
        print('<!DOCTYPE html>')
        print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
        print('<head> <title> Easter Date </title> </head>')
        print('<body>')
        print('<br><br><br><br><br><br>')
        print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
        print(f'<p3> {p}<sup>rd</sup> of {month} {y} <br> </p3>')
        print(f'<p4> {day}/{x}/{y} </p4>')
        print('</body>')
        print('</html>')

    else:
            print('Content-Type: text/html; charset=utf-8')
            print('')
            print('<!DOCTYPE html>')
            print('<link rel="stylesheet" type="text/css" href="../Form_Easter.css">')
            print('<head> <title> Easter Date </title> </head>')
            print('<body>')
            print('<br><br><br><br><br><br>')
            print(f'<p2>The Easter date of the year {y} is on the, <br> </p2>')
            print(f'<p3> {p}<sup>th</sup> of {month} {y} <br> </p3>')
            print(f'<p4> {day}/{x}/{y} </p4>')
            print('')
            print('</body>')
            print('</html>')
