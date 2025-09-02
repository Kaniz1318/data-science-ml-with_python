#1.Method Overriding

class GrandFather():
    def greet(self):
        print("GrandFather says")
        
class Father(GrandFather):
    def greet(self):
        print("Father says")
        
class Children(Father):
    def greet(self):
        print("Children says")
        
gf=GrandFather()
f=Father()
c=Children()
gf.greet()
f.greet()
c.greet()

print("------------")

#2.Method Overloading
class Shape:
    def area(self,a,b=10):
        return a*b
a=Shape()
print(a.area(12))
print(a.area(12,12))