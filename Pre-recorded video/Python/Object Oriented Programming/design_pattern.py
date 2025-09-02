#Singleton
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("1st object is created")
            cls._instance=super(Singleton,cls).__new__(cls)
        return cls._instance
ob1= Singleton()
ob2=Singleton()
print(ob1 is ob2)

print("---------")

#2.Factory Design Pattern
# Vehicle Classes
class Car:
    def drive(self):
        print("Driving a car")

class Bike:
    def drive(self):
        print("Riding a bike")

class Bus:
    def drive(self):
        print("Driving a bus")

# Factory Class
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "bike":
            return Bike()
        elif vehicle_type.lower() == "bus":
            return Bus()
        else:
            raise ValueError("Unknown vehicle type")

# Using the Factory
vehicle1 = VehicleFactory.get_vehicle("car")
vehicle1.drive()     # ✅ Driving a car

vehicle2 = VehicleFactory.get_vehicle("bike")
vehicle2.drive()     # ✅ Riding a bike

vehicle3 = VehicleFactory.get_vehicle("bus")
vehicle3.drive()     # ✅ Driving a bus
print("---------")

#Builder Design Pattern

class Computer:
    def __init__(self,cpu,ram,storage):
        self.cpu=cpu
        self.ram=ram
        self.storage=storage
    def __str__(self):
        return f"Computer with {self.cpu} CPU,{self.ram} RAM,{self.storage} STORAGE."    
class ComputerBuilder:
    def __init__(self):
        self.cpu=None
        self.ram=None
        self.storage=None
    def set_cpu(self,cpu):
        self.cpu=cpu
        return self
    def set_ram(self,ram):
        self.ram=ram
        return self
    def set_storage(self,storage):
        self.storage=storage
        return self
    def build(self):
        return Computer (self.cpu,self.ram,self.storage)
builder=ComputerBuilder()
computer=builder.set_cpu("Intel core i9").set_ram("32gb").set_storage("1TB SSD").build()
print(computer)