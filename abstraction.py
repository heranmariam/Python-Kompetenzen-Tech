##################### Abstraction  Example ##############################

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
        
#     def area(self):
#         return self.__length * self.__width
#     def perimeter(self):
#         return 2*(self.__length + self.__width)
    
# rect = Rectangle(5,3)
# print (rect.area())
# print (rect.perimeter())

# create a circle class that represents a cicle with a given radius. The class should use data abstraction by keeping the radius as a private attribute implementation the method for calculating area and circumference of circles? ############################

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        
    def area(self):
        return 3.14*self.__radius*self.__radius
    
    def circumference(self):
        return 2*(3.14*self.__radius)
    
cir= Circle(5)
print (cir.area()) 
print (cir.circumference())


