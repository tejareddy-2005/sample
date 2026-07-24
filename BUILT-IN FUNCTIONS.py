#built-in functions
#print(dir())
#print(dir("__builtins__"))
#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(tuple(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"teja")
print(c)

c["d"]="python"
print(c)'''


#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''
'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''
'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''
'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''


'''#zip()->we can combine multiple collections
#into one collection
a=[10,20,30,40,50,60]
names=["teja","raja","baja","kaja","leja"]
print(a+names)

'b=zip(a,names)
print(b)
c=list(zip(a,names))
print(c)
c=tuple(zip(a,names))
print(c)
c=set(zip(a,names))
print(c)
c=dict(zip(a,names))
print(c)'''

#enumerate()->we can give counte to the collection

'''names=["pandu","gopi","lokesh","venkey","chandu"]
for i in range(len(names)):
    print(i,names[i])'''


'''b=list(enumerate(name))
print(b)

b=list(enumerate(name,10))
print(b)

b=dict(list(enumerate(name,100))
print(b)'''

#ASCII
#CHR()
#ORD()
'''print(chr(65))
print(chr(90))
print(chr(92))
print(ord("a"))
print(ord("z"))
print(ord("y"))'''

'''for i in range(97,123):
     print(chr(i),end=" ")
for i in range(65,91):'''

'''a=input("enter letter :")
for ch in a:
    print(ch,"-",ord(ch))'''
#BMI=18.5->under weight
#18.5 to 24.5->healthy weight
#24.5 to 29.5->over weight
#30 t0 above -> obesity
'''while True:
    w=float(input("enter weight:"))
    h=float(input("enter height:"))
    b=w/(h)**2
    print(b)
    if b<=18.5:
        print("U W")
    elif b>=18.5 and b<24.5:
        print("H W")
    elif b>=24.5 and b<29.5:
        print("O W")
    elif b>30.5:
        print("obesity")'''
       

#annonymous func are name less funcand we use keyword called as lamda to create annonymous func.  
#write a func to calculate 2*x+5 where x=5
'''def cal():
    x=5
    print(2*x+5)
cal()

def f():
    x=int(input())
    print(2*x+5)
f()'''
#syntax
#use lamda arg:expr
'''a=lambda x:2*x+5
print(a(5))

a=int(input())
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda x,y:x*y
print(a(3,3))'''
'''x=int(input())
y=int(input())
a=codegnanlambda x,y:x*y
print(a(x,y))'''

#codegnan,CODEGNAN
'''a="codegnan"
b=lambda a:a.upper()
print(b(a))'''

'''a=lambda a:a.upper()
print(a("codegnan"))'''

'''a=lambda a:a.title()
print(a("python course"))
#firatname+lastname=fullname
a=input("fname:")
b=input("lname:")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''#generator
a,b=[x for x in input("enter values:").split(" ")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter
'''a=[10,13,50,100,127,39,45,67,200]
for i in a:
    if i%2==0:
        print(i)'''
'''a=[10,13,50,100,127,39,45,67,200]
b=list(filter(lambda x:x%2==0,a))
print(b)'''

a=[[],(),{},"",None,5,8.9,"kaja",5+9j,True,False]
b=list(filter(None,a))
print(b)





























       
