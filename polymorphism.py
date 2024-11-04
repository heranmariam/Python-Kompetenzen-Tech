class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.Width=width
        self.Height=height
    def area(self):
        return self.Width*self.Height
            
class Triangle(Shape):
    def __init__(self,base,height):
        self.Base=base
        self.Height=height
    def area(self):
        return 0.5*self.Base*self.Height
    
class Circle (Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    
shape1=Rectangle(2,5)
shape2=Triangle(8,9)
shape3= Circle(2)
print(shape1.area())
print(shape2.area())
print(shape3.area())