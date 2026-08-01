#MODULE:-
#A module in python is a single python file it consist python code
#it tipically consist of funcs ,classes and variables that can be used in other python scripts or programm
#ex:- math.py,random.py or my module.py
#PACKAGE:-
#package :- A package in python is a directory containing one or more python modules and an --init--.py
#that init.py file can be empty or contain initialisation code for the package
#Ex:- numpy,pandas ,requests,django
#LIBRARY:-
#library:-It consists of both modules and pacakges
#Ex:-numpy,pandas,matlotlib
#NOTE:--every python file is a module and import is a keyword and every python file is saved internally with variable name as __main__
'''def greeting(name):
    print("welcome",name)'''

'''a=4
b=8
print(a+b)'''

'''a=int(input())
b=int(input())
print(a+b)'''

'''details={"idnos":[10,20,30],
         "name":["teja","raja","baja"],
         "marks":["60,70,80"]}'''
'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''

'''#math module
import math
print(math.pi)
print(math.pi*4)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(6.9))
print(math.floor(3.11))'''

'''from math import pi,sqrt,log,tan
print(pi)
print(sqrt(4))
print(log(6))
print(tan(45))'''

'''import sys
print(sys.version)
print(sys.path)'''

'''OS MODULE
import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\Sita\\Desktop\\python"))
print(os.listdir())'''

#RANDOM MODULE
#Random module is used to generate ramdon numbers in python,randint func is used this func is defined random module
'''import random
a=random.sample(range(1,20),15)
print(a)'''
'''import random
a=random.randint(50,60)
print(a)'''
'''import random
a=[30,40,50,60,70]
b=random.choice(a)
print(b)'''

#DICE ROLL
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again? (y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid option")'''
