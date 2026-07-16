#FUNCTION:
#A function is a block of code that is used to perform a single or multiple task
#python gives in built function like print,you can make your own function alsoand thse are called user defined function
#python blogs begin with the key word def followed by the function name and peranthasis()()
'''a=10
b=20
print("sum is",a+b)
print("diff is",a-b)
print("product is",a*b)
a=100
b=200
print("sum is",a+b)
print("diff is",a-b)
print("product is",a*b)
a=1000
b=2000
print("sum is",a+b)
print("diff is",a-b)
print("product is",a*b)'''

'''def calculate(a,b):
    print("sum is",a+b)
    print("diff is",a-b)
    print("product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''


'''def calculate(a,b):
    print("div is",a//b)
    print("mod is",a%b)
    print("pow is",a**b)
calculate(1,2)
calculate(4,2)
calculate(2,3)'''

'''def add(a,b):
    print(a+b)
add(4,5)'''

'''def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
cal()'''

'''def cal():
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
    cal()
cal()'''

'''def fullname():
    fname=input("first name")
    iname=input("last name")
    print((fname+" "+iname).title())
fullname()'''

#difference print and return
#print just shows the human user input in a console
#return will the terminate the function and gives back a value fro, the function
'''def mul(a,b):
    print(a*b)
mul(3,5)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''

#print v/s return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(5,6)'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(add(6,8))'''

#splitbill()
'''def splitbill():
    tbm=float(input())
    people=int(input())
    bill=tbm/people
    print("per",amount)
splitbill()'''

'''def splitbill():
    tb=float(input())
    people=int(input())
    bill=tb/people
    print("per:{}".format (bill))
    print(f"per(bill)")
splitbill()'''

'''def cal():
    a=int(input())
    b=int(input())
    option=int(input())
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
    else:
        print("invalid")
cal()'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    option=int(input('''choose the option
                           1.add
                           2.sub
                           3.mul'''))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''

                           
#keyword and positional argumenents
                    
'''def details(id,name,mailid):
    id=10
    name="teja"
    mailid="teja@.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="teja@.com")
'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id="10",name="teja",mailid="teja@.com")
details(id="10",name="kaja",mailid="kaja@.com")
details(10,"raja","r@.com")
details("b@.com",30,"baja")
details(mailid="r@.com",id=55,name="roja")
'''
