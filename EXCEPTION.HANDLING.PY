#EXCEPTION HANDLING

#TRY     :-Instructions from which we are expecting the exceptions

#EXCEPT  -> exceptions are raised in try block it eill be handled by this block

#ELSE    ->optional(no.exceptions)

#FINALLY ->always it will display

'''while True:
    try:
        a=int(input("a value:"))
        b=int(input("b value:"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no execeptions")
    finally:
        print("program ends....")'''
        
#Regular expressions
#regular expreesion are opoerfull tools(modules) embedded in python which is mainly used
#to find the pattern within in the given strings or statements or files and we mainly used for text manification
#rex
'''a="teja"
print(a)'''

'''a="teja\nis\tfrom\nengland"
print(a)'''
'''a=r"teja\nis\tfrom\nEngland"
print(a)'''
#compile(),search(),findall(),split(),sub()

#sequence characters
'''\w->it matches alphanumeric
\W->it matches non_alpha numeric
\d->it matches any digit
\D->it matches non digit
\s->it represents white spaces
\S->it represents non white spaces'''
#compile()
import re
a="mat cat cap maths money cash code cup dog donkey"
'''b=re.compile(r"m\w\w\w\w")
print(b)
#search()
c=b.search(a)
print(c)
b=re.search(r"m\w+",a)
print(b)
#findall()
b=re.findall(r"e\w+",a)
print(b)'''
#split()
'''d=re.split(r"m",a)
print(d)

e=re.split(r"\S",a)
print(e)

#sub()
f=re.sub("m","a",a)
print(f)'''

'''b="year 2026 month 4 date 2
c=re.findall(r"\d'''

e="code dog donkey"
f=re.findall(r"do\w+",e)
print(f)

d=re.findall(r"\bd\w+",e)
print(d)
           
