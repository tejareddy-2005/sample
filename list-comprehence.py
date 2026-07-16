# list comprehension
a=["codegnan","python","course"]
#["codegnan","python","c ourse"]
#print(a.upper())

'''b=str(a)
print(b.upper())'''

'''for i in a:
     print(i.upper(),end=",")'''

'''b=[]
for i in a:
   b.append(i.upper900
print(b)'''
#syntax
#a=[expr for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

#task
'''a=["vij","hyd","viz"]
a=[i.title() for i in a]
print(a)'''

'''a=[1,2,3,4,5,6,7,8,9]
a=[i**2 for i in a]
print(a)'''

#if use=age in list comprehension
'''a=15
b=[i for i in range(a)]
print(b)'''
a=15
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i for i in range(16) if i%2!=0]
print(a)'''

'''a=21
a=[i*i for i in range(21) if i%2==0]
print(a)'''

a=["apple","banana","grapes","mango","kiwi","dragon","berry"]
'''b=[i for i in a if "a" in i]
print(b)'''
'''b=[i for i in a if "a" not in i]
print(b)'''

#no-elif usage in list a comprehension

#if-else usage
'''a=[i*i if i%2==0 else i*5 for i in range(31)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]
print(c)
