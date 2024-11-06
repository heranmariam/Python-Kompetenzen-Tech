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


############# WAPP with a parent class Vehicle and a derived class car that inherits from Vehicle which has attributes ,model ,brand and ################# 
################################  methods to print Vehicles infomation and is Electric or not? ##################################




# class Vehicle :
#     def __init__ (self, model, brand):
#         self.model = model
#         self.brand = brand
        
#     def is_electric_vehicle (self):
#         return False
    
#     def vehicle_info (self):
#         print ( self.model,self.brand)
    
# class Car (Vehicle):
#     def is_electric_vehicle (self):
#         return True



# Vehicle1= Vehicle("model", "brand")
# print (Vehicle1.is_electric_vehicle() )

# car = Car("1897", "yamaha")
# print (car.is_electric_vehicle() , Vehicle1.vehicle_info()) 




## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TYPES OF INHERITANCE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

############################# (1); Single Inheritance ###############################

# class Animal:
#     def sound (self):
#         return "some genric Sound"
    
# class Dog (Animal):
#     def bark (self):
#         return "woof"
    
    
# dog = Dog()
# print (dog.sound()) 
# print (dog.bark())

############################# (2); Multiple Inheritance ################################



# class Father:
#     def show_father(self):
#         return "father's traits"
    
# class Mother:
#     def show_mother(self):
#         return "Mother's traits"
    
# class Child(Father, Mother):
#     def show_child(self):
#         return "child's traits"
    
# child = Child()
# print (child.show_father())
# print (child.show_mother())
# print (child.show_child()) 

########################### (3); Multi Level Inheritance ######################################


# class Vehicle:
#     def move(self):
#         return "Vehicle is moving"
    
# class Car (Vehicle):
#     def wheel(self):
#         return " Car has 2 wheels"
    
# class ElectricCar (Car):
#     def battery(self):
#         return "Battery powered car"

# tesla= ElectricCar()
# print (tesla.move())
# print (tesla.wheel())
# print (tesla.battery())



########################### (4); Hierarchial Inheritance ######################################

# class Animal:
#     def sound(self):
#         return "Animal Sound"
    
# class Dog(Animal):
#     def bark (self):
#         return "wolf!!!"
    
# class Cat(Animal):
#     def meow (self):
#         return "Meow!!!"

# dog = Dog()
# cat = Cat()
# print (dog.sound())
# print (dog.bark())
# print (cat.sound())
# print (cat.meow())


# Q): Create a base class Animal with a method eat that returns "Eating". 
# Create a derived class Bird that inherits from Animal and has an additional method fly that returns "Flying". 
# Finally, create another derived class Parrot that inherits from Bird and adds a method speak that returns "Talking".


# class Animal:
#     def eat (self):
#         return "Eating"
    
# class Bird(Animal):
#     def fly (self):
#         return "Flying"
    
# class Parrot(Bird):
#     def speak (self):
#         return "talking"
    
# parrot = Parrot()
# print (parrot.eat())
# print (parrot.fly())
# print (parrot.speak() )



# Q): Create a base class Appliance with a method power_source that returns "Electricity".
# Then, create two derived classes: WashingMachine and Refrigerator, both inheriting from Appliance.
# Each class should have its own method (wash in WashingMachine that returns "Washing clothes" and cool in Refrigerator that returns "Cooling food").

# class Appliance: 
#     def power_source (self):
#         return "Electricity"
    
# class WashingMachine(Appliance):
#     def wash (self):
#         return "Washing clothes"
    
# class Refrigerator(Appliance):
#     def cool (self):
#         return "Cooling food"
    
# washing_machine = WashingMachine()
# cooling_machine = Refrigerator ()

# print (washing_machine.power_source())
# print (washing_machine.wash())
# print (cooling_machine.power_source())
# print (cooling_machine.cool()) 


########################### (5); Hybrid Inheritance  ######################################



class Vehicle:
    def vehicle_info(self):
        print ("inside vehicle class")
        
class Car(Vehicle):
    def car_info(self):
        print ("inside car class")
        
class Truck(Vehicle):
    def truck_info(self):
        print ("inside truck class")
        
class SportsCar (Car, Vehicle):
    def sports_car_info(self):
        print ("inside sportscar class")
        
        
s_car = SportsCar()
s_car.vehicle_info ()
s_car.car_info ()
s_car.sports_car_info ()


## I.Q) Create a base class called Animal with a method animal_info that prints "Inside Animal class." Then, create two other derived classes:

#     Mammal: A class that inherits from Animal and has a method mammal_info that prints "Inside Mammal class."
#     Bird: A class that also inherits from Animal and has a method bird_info that prints "Inside Bird class."

# Next, create a Bat class that inherits from both Mammal and Animal. Add a method bat_info in the Bat class that prints "Inside Bat class."


# class Animal:
#     def animal_info(self):
#         print ("Inside Animal class")
        
# class Mammal (Animal):
#     def mammal_info(self):
#         print ("Inside mammal class")
        
# class Bird (Animal):
#     def bird_info(self):
#         print ("Inside Bird class")
        
# class Bat (Mammal,Animal):
#     def bat_info(self):
#         print ("Inside bat class")
        
# b_ans = Bat()
# b_ans.animal_info()
# b_ans.mammal_info()
## b_ans.bird_info()   # this line has some kind of error
# b_ans.bat_info()

