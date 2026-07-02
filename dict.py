Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict
a={"name":"pooja","city":"vij"}
print(a)
{'name': 'pooja', 'city': 'vij'}
type(a)
<class 'dict'>
b={5,6,7,8,9,"name"}
type(b)
<class 'set'>
a={"name":"pooja","mailid":"tejareddydusani@gmail.com","mobileno":7671098072}
print(a)
{'name': 'pooja', 'mailid': 'tejareddydusani@gmail.com', 'mobileno': 7671098072}
a.keys()
dict_keys(['name', 'mailid', 'mobileno'])
a.values()
dict_values(['pooja', 'tejareddydusani@gmail.com', 7671098072])
a.items()
dict_items([('name', 'pooja'), ('mailid', 'tejareddydusani@gmail.com'), ('mobileno', 7671098072)])
a={"course":"python":"institute":"codegnan"}
SyntaxError: invalid syntax
a={"course":"python","institute":"codegnan"}
a.update({"name":"teja"})
a
{'course': 'python', 'institute': 'codegnan', 'name': 'teja'}
a.update({"year":2026,"month":7})
a
{'course': 'python', 'institute': 'codegnan', 'name': 'teja', 'year': 2026, 'month': 7}
a={"year";2026,"month":"july
   
SyntaxError: unterminated string literal (detected at line 1)
a={"year";2026,"month":"july"}
   
SyntaxError: invalid syntax
a={"year":2026,"month":"july
   
SyntaxError: unterminated string literal (detected at line 1)
KeyboardInterrupt


a={"year":2026,"month":"july"}
   
a.setdefault("date",2)
   
2

a
   
{'year': 2026, 'month': 'july', 'date': 2}
a={"time":12,"hour":1,"min":3}
   
a.pop()
   
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("time")
   
12
a.popitem()
   
('min', 3)
a
   
{'hour': 1}
a={"college":"urce","branch":"aiml"}
   
a.get("college")
   
'urce'
a["branch]
  
SyntaxError: unterminated string literal (detected at line 1)



a["branch"]
  
'aiml'
a
  
{'college': 'urce', 'branch': 'aiml'}
a.get("cse")
  
a
  
{'college': 'urce', 'branch': 'aiml'}
a={"hour":12,"min":3,"sec":60}
  
a.copy()
  
{'hour': 12, 'min': 3, 'sec': 60}
a
  
{'hour': 12, 'min': 3, 'sec': 60}
a.clear()
...   
>>> a
...   
{}
>>> b={}
...   
>>> b.update({"name":"teja"})
...   
>>> b
...   
{'name': 'teja'}
>>>  a={"name":"teja","course":"python","year":2020}
...   
SyntaxError: unexpected indent
>>> a={"name":"teja","course":"python","year":2020}
...   
>>> len(a)
...   
3
>>> a={"name":"teja","city":"vjy","name":"teja"}
...   
>>> print(a)
...   
{'name': 'teja', 'city': 'vjy'}
>>> a={"name1":"teja","city":"vij","name2":"teja"}
...   
>>> print(a)
...   
{'name1': 'teja', 'city': 'vij', 'name2': 'teja'}
>>> a={"idnos":[10,20,30],"names":["teja","raja","kaja"],"marks":[60,70,80]}
...   
>>> print(a)
...   
{'idnos': [10, 20, 30], 'names': ['teja', 'raja', 'kaja'], 'marks': [60, 70, 80]}
>>> type(a)
...   
<class 'dict'>
>>> a.keys()
...   
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
...   
dict_values([[10, 20, 30], ['teja', 'raja', 'kaja'], [60, 70, 80]])
>>> a.items()
...   
dict_items([('idnos', [10, 20, 30]), ('names', ['teja', 'raja', 'kaja']), ('marks', [60, 70, 80])])
