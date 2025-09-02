#Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):  # শুধু structure দিলাম
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d = Dog()
d.sound()   # Bark

c = Cat()
c.sound()   # Meow

print("-----------")

#Encapsulation
class GrandFather():
    def __init__(self):
        self.name="Hello"  #public
        self._age=30  #protected
        self.__khajana=30000  #private
    def greet(self):
        print("GrandFather says")
        
class Father(GrandFather):
    def greet(self):
        print(f"Father says.{self._age}")
        print(f"Father says.{self._GrandFather__khajana}")
        
        
class Children(Father):
    def greet(self):
        print("Children says")
        
gf=GrandFather()
f=Father()
c=Children()
gf.greet()
f.greet()
c.greet()
print(gf.name)
print(gf.__khajana)  #=>output ashbena public na tai,jara inherit kore tarai kebol access korte pare,tai father theke access kora gese
