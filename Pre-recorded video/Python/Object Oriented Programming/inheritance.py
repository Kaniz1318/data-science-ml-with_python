#1.Single inheritance

class GrandFather:
    def __init__(self,color,first_name):
        self.color=color
        self.first_name=first_name
        
        
class Father(GrandFather):
    def __init__(self,hobby,color,first_name):
        super().__init__(color,first_name)
        self.hobby=hobby
        
gf1=GrandFather("Red","Chowdhury")
f1=Father("Cricket","Red","Chowdhury")
print(f1.first_name)
print(f1.hobby)
print("--------------")    
    
#1.Multiple inheritance
class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

    def gf_method(self):
        print("I am from Grandfather")


class Father:
    def __init__(self, hobby):
        self.hobby = hobby

    def father_method(self):
        print("I am from Father")


class Children(Father, GrandFather):   # Multiple inheritance
    def __init__(self, fashion, hobby, color, first_name):
        Father.__init__(self, hobby)              # Father constructor কল
        GrandFather.__init__(self, color, first_name)  # GrandFather constructor কল
        self.fashion = fashion


# এখন Children এর object বানাই
c1 = Children("Modern", "Badminton", "Red", "Chowdhury")

c1.gf_method()        # GrandFather থেকে
c1.father_method()    # Father থেকে
print(c1.fashion, c1.hobby, c1.color, c1.first_name)
print("--------------") 

#3.Multilevel Inheritance
class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

    def gf_method(self):
        print("I am from Grandfather")
        

class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)  # GrandFather-এর constructor কল
        self.hobby = hobby

    def father_method(self):
        print("I am from father")
        

class Children(Father,GrandFather):
    def __init__(self, fashion, hobby, color, first_name):
        super().__init__(hobby, color, first_name)  # Father constructor কল
        self.fashion = fashion
    

# এখন Children ক্লাসের object 
c1 = Children("Modern", "Badminton", "Red", "Chowdhury")

c1.gf_method()        # GrandFather থেকে
c1.father_method()    # Father থেকে
print(c1.fashion, c1.hobby, c1.color, c1.first_name)  # সব attribute print
print("--------------") 

#4.Hierarchical Inheritance

class Vehicle:
    def engine_type(self):
        print("Vehicle has an engine")
        
class Car(Vehicle):
    def num_doors(self):
        print("Car has 4 doors")
        
class Truck(Vehicle):
    def load_capacity(self):
        print("Truck can carry 10 Tons")
        
car=Car()
car.engine_type()
car.num_doors()
truck=Truck()
truck.load_capacity()
truck.engine_type()

print("--------------") 

#5.Hybrid Inheritance
class Shape:
    def area(self):
        print("Calculation area...")
class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides")
class Rectangle(Polygon):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    
rec=Rectangle(10,5)
rec.sides()
print(rec.area())
rec.area()


    