a=[1,10,23,24,26,90]

result=[]

#Normal way
for i in a:
    if i%2==0:
        result.append(i)
print(result)
#print(10/3)
#print(10//3)
#3)10(3
#   9
#--------
 #  1  
#print(10%3)

#List comprehension
new_result = [i for i in a if i%2==0]
print(new_result)

b=[1,2,3,4,5]
b_new=[]
#b_new=[i**2 if i%2==0 else i for i in b]
#print(b_new)

for i in b:
    if i%2==0:
        b_new.append(i**2)
    else:
        b_new.append(i)
print(b_new)