a=[1,2,3,4,"a",5,6,7]

print(type('b'))

for i in a:
    if type(i)==type('b'):
        break   #loop end kore
    else:
        print(i)
        
print("--------------")
for i in a:
    if type(i)==type('b'):
        continue  #ignore kore
    else:
        print(i)

