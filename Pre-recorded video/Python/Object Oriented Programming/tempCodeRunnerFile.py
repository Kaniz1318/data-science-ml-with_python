class GrandFather:
    def __init__(self,color,first_name):
        self.color=color
        self.first_name=first_name
    def gf_method(self):
        print("I am from Grandfather")
        
class Father(GrandFather):
    def __init__(self,hobby):
        self.hobby=hobby
    def father_method(self):
        print("I am from father")
        
class Children(Father,GrandFather):
    def __init__(self,fashion,hobby,color,first_name):
        Father.__init__(self,hobby)
        GrandFather.__init__(self,color,first_name)
        self.fashion=fashion 
    
           
c1=GrandFather("Test","Badminton","Red","Chowdhury")
c1.gf_method()
c1.father_method()
print(c1.fashion, c1.color,c1.first_name)
