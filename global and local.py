#variables inside and outside the function is called local and global variables
#A variable is deffined above the function is acccesable to the enteire global space is called global variable
# variable is inside the function iis called local variable
#first case of global variable
'''a=4
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)'''
#second case of global variable
'''a=2
def check2():
    a=5
    a=a**2
    print("inside valueis",a)
check2()
print("outside value is",a)'''

#third case of both global and local variable
'''a=6
def check3():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    a=13
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("a value is",b)'''

#usage of globle keyword
#when user wants access the globale variable inside the function directly and carry forward updated value even outside the function then we need to globle keywords
a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("updated value is",a)
    #global b
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)
