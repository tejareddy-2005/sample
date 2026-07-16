#keyword and positional argumenents
                    
'''def details(id,name,mailid):
    id=10
    name="teja"
    mailid="teja@.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="teja@.com")'''


'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id="10",name="teja",mailid="teja@.com")
details(id="10",name="kaja",mailid="kaja@.com")
details(10,"raja","r@.com")
details("b@.com",30,"baja")
details(mailid="r@.com",id=55,name="roja")'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("sugar",100)'''

'''def grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")''' 

'''def grocery(item="ghee",price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(500)'''

#cake_name,price,qty
'''def bekary(name,price,qty):
    print("name is %s" %name)
    print("price is %.2f" %price)
    print("qty is 0.2" %qty)
bekary("red",15,0.2)'''

# * Arguments(* is used to unpack the elements)
'''a=[1,3,4,5,6,7,8]
print(a)
print(*a)

a=(1,2,3,4,5,6,7,8)
print(a)
print(*a)

a={1,2,3,4,5,6,7,8,9}
print(a)
print(*a)
'''

''''b={"name":"teja","city":"nyd"}
print(b)
print(*b)'''

'''c="python"
print(c)
print(*c)'''

'''a,b,c=2,3,4,5,6,7
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=1,2,3,4,5,6,7
print(a)
print(*b)
print(c)'''

'''*a,b,c=1,2,3,4,5,6,7
print(*a)
print(b)
print(c)'''

'''a,b,*c=1,2,3,4,5,6,7
print(a)
print(b)
print(*c)'''

'''a,b,c="teja"
print(a)
print(b)
print(c)'''

'''*a,b,c="teja"
print(*a)
print(b)
print(c)'''


