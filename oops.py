#CLASS-> A class contains attributes,variables or methods and func that can be MANIPULATED date
#-> A class is the blue print of an objects
#-> Methods or func that can be define inside the body of the class
#-> An object is an initiation of a class

#FLOU PILLARS OF OPPS
#1)polyphorpism   ->operator over loading,operator overriding,method overloading,method overriding
#2)Inheritence    ->single,multiple,multilevel,hybrid,hieraricle
#3)encapslulation ->public data,_protect data,__private data
#4)obstraction    ->obstract class,obstract method

#OOPS
#SYNTAX
'''class classmate():
    #attributes
    name="teja"
    age=99
    place="hyd"
    def fname(method_name):
        print("statements.............")
a=classmate()
a.fname()'''
#class declaration
'''class Details():
    name="teja"
    age=99
    place="us"         +++++++++++
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''
#object instantiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("teja",99,"hyd")
a.display()
b=Details()
print(dir(a))
b.data("kaja",98,"hyd")
b.display()'''
#object initialization
"""class Details():
    #constructor creater
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place 
    def display(self):
        print(self.name,self.age,self.place)
a=Details("Teja",99,"us")
print(dir(a))
a.display()"""
'''#runtime input()
class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

'''#diff b/w _ and __ :-> When user wants to create a variable with double leading __underscore our python interpretor
treace a speacial variable to avoid name confix with method and inner classes '''
'''class employee():
    def __init__(self):
        self.name="teja"
        self._mailid="teja@22005"
        self.__salary=1#private variable
class employee1():
    def __init__(self):
        self.name="teja"
        self._mailid="teja@22005"
        self.__salary=2
class employee2():
    def __init__(self):
        self.name="teja"
        self._mailid="teja@22005"
        self.__salary=3
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee__salary)
b=employee1()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._employee1__salary)
c=employee2()
print(dir(a))
print(c.name)
print(c._mailid)
print(c._employee2__salary)
print(c._employee2__salary)'''

#Operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(b))
print(a.__pow__(2))
print(a.__ge__(b))
print(a.__le__(b))
print(a.__eq__(2))
a=[2,3,4,5,6,7,8];b=[4,5,6,7,8,9,10]
print(a+b)
print(a.__add__(b))
print(b.__getitem__(5))
a="code";b="gnan"
print(a+b)
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b))
print(a.__add__(" "+b).title())
print("teja".__add__("d"))'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(4)
print(x+y)'''
#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is:",a*b)
        else:
            print("Program ends...")
a=new()
a.sum()
a.sum(2,4,6)
a.sum(6,3)'''
#tasks
'''class car():
    def vehical(self):
        print("nano")
class bike():
    def vehical(self):
        print("XL100")
a=car()
b=bike()
a.vehical()
b.vehical()'''
#2.single inheritance
'''class RBI():
    cash=10
    def available_cash(cls):
        print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=5
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''
#multiple inheritance
'''class father():
    x=int(input())
    def height(jp):
        print("height is",jp.x)
class mother():
    y=int(input())
    def weight(jp):
        print("weight is",jp.y)
class kid(father,mother):
    z=int(input())
    def dob(jp):
        print("dod is",jp.z)
a=kid()
a.height()
a.weight()
a.dob()'''



#multi level
'''class sumanth():
    def land(self):
        print("1 acres")
class parent(sumanth ):
    def house(self):
        print("house")
class child(parent):
    def plate(self):
        print("plate")
a=child()
a.land()
a.house()'''


#hierarchical inheritence--> it ia a where one parent class is inherted by multiple childs classes
'''class employee():
    def company(self):
        print("ITBT")
class trainer(employee):
    def subject(self):
        print("teach the code")
class developer(employee):
    def subject(self):
        print("develop the code")
a=developer()
b=trainer()
b.company()
b.subject()
a.company()
a.subject()'''

'''class person():
    def details(self):
        print("kaja")
class Trainer(person):
    def k(self):
        print("teaching")
class student(person):
    def p(self):
        print("study")
class program_manager(Trainer,student):
    def t(self):
        print("Manager")
a=program_manager()
a.details()
a.k()
a.p()
a.t()'''
#super()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child (parent):
    def __init__(self,name,age):
        self.age=age
        self.name=name
        print("child constructor")
a=child("teja",99)
print(dir(a))
print(a.name)
print(a.age)'''

'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child (parent):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("teja",99)
print(dir(a))
print(a.name)
print(a.age)'''

#encapsulation
#public data
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''
#_protect data
'''class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)
'''#private data
'''class parent():
    __privatedata="pandu"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj=child()
obj.method1()
obj.method2()'''

#Abstract : Hiding unneccessary information from user is call abstraction
#abstract class:- In this we have one more abstract methods is known as abstraction class.
#Abstract Method :- The method declared without implementation these called abstract method
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()
 
from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''
#Decorator

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("codegnan")
obj1=A()
obj1.method1()'''#error

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("python course")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data science")
    def method3(self):
        print("ML")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''





























    
 

 


      































