#ekta class banabo name Car, etar object banabo
#brand,model
class Car:
    def __init__(self):   #self==ei car class er object ke indicate kore
        self.brand=""
        self.model=""
        
car1 = Car()
car1.brand="Toyota"
car1.model="Corolla"
print(car1.brand)
print(car1.model)

car2 = Car()
car2.brand="Honda"
car2.model="Civic"
print(car2.brand)
print(car2.model)


#__init__()  : Dunder(double underscore method),Constructor,no return
#constructor : 3types
#1.Default constructor-->
class Car:
    def __init__(self):   #self==ei car class er object ke indicate kore
        self.brand=""
        self.model=""
        

car1 = Car()
car1.brand="Toyota"
car1.model="Corolla"
print(car1.brand)
print(car1.model)


car2 = Car()
car2.brand="Honda"
car2.model="Civic"
print(car2.brand)
print(car2.model)
print("----------------")

#2.parameterized constructor
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
car1 = Car("Toyota","Corolla")
print(car1.brand)
print(car1.model)


car2 = Car("Honda","Civic")
print(car2.brand)
print(car2.model)

print("----------------")
#Default value constructor
class Car:
    def __init__(self, brand="Toyota", model="Corolla"):
        self.brand = brand
        self.model = model

# কিছু না দিলে default parameter নেবে
car1 = Car()
print(car1.brand)   # Toyota
print(car1.model)   # Corolla

# দুইটা parameter দিলে নিজেরটা নেবে
car2 = Car("Honda", "Civic")
print(car2.brand)   # Honda
print(car2.model)   # Civic

# শুধু একটাই parameter দিলে
car3 = Car("BMW")   # এখানে শুধু brand দিলাম, model default থাকবে
print(car3.brand)   # BMW
print(car3.model)   # Corolla


print("----------------")
#Method inside class
class Car:
    def __init__(self, brand, model):   # constructor define করা হলো
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}\nCar Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display_info()
car2.display_info()



