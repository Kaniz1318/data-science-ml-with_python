a=[1,2,3,'Naim','Fahim',8.9,3.4]
#list mutable
a[0]=100
print(a)
print(a[-1])
print(len(a))

#s= "HELLO"-->['H','E','L','L','O']
s="He  llo"
print(list(s))

a.append([1,2,3])
print(a.index(300))
a.reverse()
print(a)

#tuple  immutable
t=(1,2,3)
t[0]=100
print(t) #output ashbena

t=(1,2,3)
#t[0]=100
t_r=tuple(reversed(t))
print(t) 
print(t_r)



