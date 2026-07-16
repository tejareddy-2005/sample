Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
typr(b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    typr(b)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("DSA")
a
['python', 'java', 'c', 'c++', 'DSA']
#extend
a=["ml","ai","ds"]
a.extend(["c","c++","python"])
a
['ml', 'ai', 'ds', 'c', 'c++', 'python']
#insert()
b=["vij","hyd"]
b.insert(1,vij)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.insert(1,vij)
NameError: name 'vij' is not defined
b.insert(1,"krl")
b
['vij', 'krl', 'hyd']
#index
a=["black","green","white","blue"]
a.index("blue")
3
a.index("green")
1
#copy
a.copy
<built-in method copy of list object at 0x0000020F7B2DC500>
a.copy()
['black', 'green', 'white', 'blue']
b=a.copy()
b
['black', 'green', 'white', 'blue']
#count
b.count("green)
        
SyntaxError: unterminated string literal (detected at line 1)
b.count("green")
        
1
d=["re","hi","bye","bye"]
        
d.count("bye")
        
2
#sort
        
a=["graphes","mango","banana","apple"]
        
a.sort()
        
a
        
['apple', 'banana', 'graphes', 'mango']
b=[5,4,6,7,2,9,7,5]
        
b.sort()
        
b
        
[2, 4, 5, 5, 6, 7, 7, 9]
#reverse
        
a=[5,4,5,6,7,89,96,4]
        
a.reverse()
        
a
        
[4, 96, 89, 7, 6, 5, 4, 5]
b=["vij","hyd","knr"]
        
b.reverse()
        
b
        
['knr', 'hyd', 'vij']
#pop
        
a=["vij","hyd","krn"]
        
a.pop()
        
'krn'
a.pop(1)
        
'hyd'
>>> a
...         
['vij']
>>> b=["c","c++","java"]
...         
>>> b.pop(2)
...         
'java'
>>> b
...         
['c', 'c++']
>>> b.remove("c")
...         
>>> b
...         
['c++']
>>> #len
...         
>>> a=["teja","raja","kaja","roja"]
...         
>>> len(a)
...         
4
>>> b="teja"
...         
>>> len(b)
...         
4
>>> c=["teja"]
...         
>>> len(c)
...         
1
>>> c
...         
['teja']
>>> a.clear()
...         
>>> a
...         
[]
>>> a.append("hi")
...         
>>> a
...         
['hi']
