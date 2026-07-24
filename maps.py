#map-> each object from a collection and forms a new collectiona
# max(),min(),sum()
'''print(max(3,4,5,6,7,8,90))
print(min(1,2,3,4,5,6,7,8,9,10))

a=(1,2,3,4,5,6,7,8,9,10)
print(sum(a))'''

'''a=[2,3,4,5,6,7,8,9]
b=[2,4,5,7,8,9,3,1]
c=list(map(max,a,b))
print(c)
c=list(map(min,a,b))
print(c)'''

'''a=int(input("data1"))
b=int(input("data2"))
print(a+b)'''

'''a,b=input("enter the names").split(",")
print(a+b)'''

'''a,b=[x for x in input("names").split(",")]
print(a+b)'''
'''a,b=map(str,input('enter the name').split(","))
print(a+b)'''
'''a,b=int(input()).split(",")
print(a+b)'''#error

'''a,b=list(int,input('enter the name').split(","))
print(a+b)'''                     

'''a=[x for x in input("names").split(",")]
print(a)'''
'''a=map(map(int,input('enter the name').split(","))
print(a+b)'''
'''a=tuple(map(int,input('enter the name').split(",")))
print(a)                     
a=set(map(int,input('enter the name').split(",")))
print(a)
a=list(map(int,input('enter the name').split(",")))
print(a)'''
'''a=tuple(map(eval,input('enter the name').split(",")))
print(a)
print(typr(a))'''

'''a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''

#marks analysis report
a=int(input("enter no of student :"))
m=[]
for i in range(1,a+1):
    ma=int(input(f"enter the student{i} marks"))
    marks.append(ma)
for i in ma:
    print(i)
print("----------- marks analyst report---------")
print(a)
print(max(m))
print(min(m))
print(sum(m))
print((sum/n))

