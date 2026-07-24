#no tuple comphrehencese in above cases if remove those braces and keep peranthasis when the out come is generator
#[expr for var i in range]
'''a=[i for i in range(16)]
print(a)
print(type)'''

#(expr for var in collection/range)
'''a=(i for i in range(16))
print(a)
print(*a)
print(type(a))'''

'''b=list(a)
print(b)'''

#print(tuple(a))
'''print(set(a))'''
#a genrator is also a function which can use as an itarator(loop) by producing group of values,where we use yield keywords

#yield vs return

#return will terminate the function where as yeild can function and go on with every successive itaration 
'''a,b=[int(x) for x in input("enter:").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter a value:").split()]
def check(a,b):
    while a<b:
        a=a+1
        #return
    return a
print(*check(a,b))'''

#yield v/s return
'''def mygen():
    #return "vij"
    #return "hyd"
    #return "vzg"
    return "vij","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "pyt"
    yield "java"
    yield "DSA"
print(*mygen())'''

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
    



