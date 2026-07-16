#if else-else
'''a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")'''
'''a=4
b=6
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")'''
'''a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''
'''a=4
b=6
if a==b:
    print("equal")
elif b<a:
    print("greater")
else:
    print("true")'''
#if-elif-else using logical operator
'''a=4
b=6
if a<b and a>b:
    print("less")
elif b>a:
    print("greater")'''
'''a=4
b=6
if a>b and a<b:
    print("less")
elif b>a:
    print("greater")'''
'''a=4
b=6
if a<=b and a>=b:
    print("less")
elif a>b:
    print("true")'''
'''a=4
b=6
if a!=b and a==b:
    print("less")
elif b!=a:
    print("not equal")'''
#logical all
'''a=10
b=15
if a<b and b>a:
    print("less")
elif a!=b or a==b:
    print("equal")
else:
    print("false")'''
#identify
'''a=5
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("flase")'''
'''a=5
if type(a) is not int:
    print("it is int")
elif type(a) is int:
    print("flase")'''
'''a=1,2,3,4,5,6,7,8
if 5 in a:
    print("in")
elif 5  not in a:
    print("not")'''
#multiple-if conditions
'''a=20
b=40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''
'''a=20
b=40
if a==b: 
    print("less")
if b<a:
    print("greater")
if a!=b:
    print("not equal")'''
'''a=20
b=40
if a==b:
    print("less")
if b>a:
    print("greater")
if a>=b:
    print("not equal")
else:
    print("true")'''
'''a=20
b=40
if a>b:
    print("true")
elif a>b:
    print("true")
else:
    print("yes")'''
 #nested if conditions
'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''
'''a=4
b=9
if a>b:
    print("less")
    if b>a:
        print("greater")'''
'''a=7
b=11
if a!=b:
    print("true")
    if a==b:
        print("greater")'''
'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")'''
'''a=13
b=15
if a==b:
    print("true")
    if b>a:
        print("greater")
else:
    print("false")'''
'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")
else:
    PRINT("NOT TRUE")'''
'''a=20
b=25
if a!=b:
    print("true")
    if b==a:
        print("greater")
    elif a<b:
        print("less")

    else:
        print("false")'''
a=int(input())
b=int(input())
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("programms ends")
    
        
