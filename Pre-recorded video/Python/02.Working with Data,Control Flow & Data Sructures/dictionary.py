#{}
#key value pair
#indexing er shujog nai
#key gulo obosshoi immutable

a={'rahim':12,'karim':14,'fahim':78,1:[1,2,3,4],2:{3,4,5}}
print(a)
print(type(a))

for i in a:
    print(i)
    
print("-------------------")

for i in a.values():
    print(i)
    
print(a.keys(),a.values())
print("-------------------")

for k,v in a.items():
    print(f"key name:{k},values:{v}")
print("-------------------")

a=[1,2,3]
b=["Mango","Banana","Apple"]

#{1:"Mango",2."Banana",3."Apple"}

print(list(zip(a,b)))

print(dict(zip(a,b)))

c=dict(zip(a,b))
print(dict(zip(a,b)))
print(c[1])


c=dict(zip(b,a))
print(dict(zip(a,b)))
print(c["Mango"])


