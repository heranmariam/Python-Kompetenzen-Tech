# class Person:  ##########  this is the Parent class  ###############
    
#     def __init__ (self, name):
#         self.name = name
        
#     def get_name(self):
#         return self.name
    
#     def is_employee(self):
#         return False
    
# class Employee(Person): ######### this is the child class  ##############
#     def is_employee(self):  ########### just parent il ninu ee code yezhuthiya mathi ,, veedum ellam yezhuthendaaa just Person ine parent aakitt call cheytha mathi ####
#         return True    ######### for the code reusablility #########
    
# employee1= Person("name1")
# print (employee1.get_name(), employee1.is_employee())

# employee2= Employee("name2")
# print (employee2.get_name(), employee2.is_employee())


#### example 2 :######
# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def speak (self):
#         return "Animal Sound"
    
# class Dog(Animal):
#     def speak (self):
#         return "wolf!!!"
    
# class Cat(Animal):
#     def speak (self):
#         return "Meow!!!"

# dog = Dog ("Buddy")
# cat = Cat ("Whisker")

# print (dog.name)
# print (dog.speak())
# print (cat.name)
# print (cat.speak())




class Vehicle :
    def __init__ (self, model, brand):
        self.model = model
        self.brand = brand
        
    def is_electric_vehicle (self):
        return False
    
    def vehicle_info (self):
        print ( self.model,self.brand)
    
class Car (Vehicle):
    def is_electric_vehicle (self):
        return True



Vehicle1= Vehicle("model", "brand")
print (Vehicle1.is_electric_vehicle() )

car = Car("1897", "yamaha")
print (car.is_electric_vehicle() , Vehicle1.vehicle_info()) 

