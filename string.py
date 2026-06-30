Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
a="python course"
len(a)
13
c=""
len(c)
0
d=" "
len(d)
1
c="heefghughurwgyufh1k2erhoiu1ty8yghwefhj2gryi13t7y"
len(c)
48
#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
a.count("a")
1
b="tejareddy"
b.count("t")
1
b.count("e")
2
#find a string

a="code"
a[1]
'o'
a.find("d")
2
a.find("e")
3
b="hello"
b.find("l")
2
#slicing is used to find the another l
b="hello"
b[2:4]
'll'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmoblie\tmailid\nclg"
print(a)
name
moblie	mailid
clg
b="name:tejareddy\nmobileno:7671098072\tmailid:tejareddydusani0@gmail.com\ncollege:vits"
print(b)
name:tejareddy
mobileno:7671098072	mailid:tejareddydusani0@gmail.com
college:vits
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="wait wait until succeed"
b.replace("wait","work")
'work work until succeed'
#lower()
a="PYTHON"
a.lower()
'python'
b="RGFYERGYUGF"
b.lower()
'rgfyergyugf'
#upper
a="python"
a.upper()
'PYTHON'
b="teja"
b.upper()
'TEJA'
b="teja"
b.captitalize()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b.captitalize()
AttributeError: 'str' object has no attribute 'captitalize'. Did you mean: 'capitalize'?
b.capitalize()
'Teja'
a="python course"
a.tittle()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
a="python course"
a.title()
'Python Course'
b="i am in the ground"
a.title()
'Python Course'
b.title()
'I Am In The Ground'
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="python course"
b.isalpha()
False
b="pythoncourse"
b.isalpha()
True
d="123456"
d.isdigit()
True
e="teja1234"
e.isdigit()
False
e.isalnum()
True
a="hello python"
a.startwith("h")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.startwith("h")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("h")
True
a.endswith("n")
True
#strip()
#lstrip(),rstrip()
a="       teja          "
a.strip()
'teja'
a.lstrip()
'teja          '
a.rstrip()
'       teja'
#split
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vijayawada"
b.split()
['i', 'am', 'in', 'vijayawada']
c="codegnan"
c.split()
['codegnan']
#join()
a="vijayawada hyd vzg"
"".join(a)
'vijayawada hyd vzg'
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
"k".join(b)
'vjakhydkvzg'
#coccatination
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="teja"
lname="reddy"
>>> print(fname+lname)
tejareddy
>>> print(fname+" "lname)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(fname+" "+lname)
teja reddy
>>> print((fanme+" "+lname).title())
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print((fanme+" "+lname).title())
NameError: name 'fanme' is not defined. Did you mean: 'fname'?
>>> print((fname+" "+lname).title())
Teja Reddy
>>> #formating
>>> a=4
>>> b=8
>>> print(a+b)
12
>>> print("the sum of the :",a+b)
the sum of the : 12
>>> g="hyd"
>>> print("form hyd",g)
form hyd hyd
>>> #dot formating
>>> a="motu"
>>> b="patlu"
>>> print("hello",a+b)
hello motupatlu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> #fstring
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> #example
>>> a=2
>>> b=4
>>> print("the product is :",a*b)
the product is : 8
