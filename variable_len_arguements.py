#variable length arguements
#variable arguements are automatically stores the tuples and used star arguements

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8,)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"teja","age":22,"place":"nyd"}
check(*d)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"teja")'''

#**(kwargs)
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["teja","kaja","raja","baja"],
         "marks":[20,30,40],
         "status":["p","a","p"]}
check2(**details)'''

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"names":["teja","kaja","raja","baja"],
         "marks":[20,30,40],
         "status":["p","a","p"]}
check2(**details)'''


#doth * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
final()
data=(2,3,4,5,6,2.3,4.5)
final(*data)
details={"year":[2024,2025,2026],
         "month":["june","july","aug"]}
final(**details)
final(*data,**details)'''


