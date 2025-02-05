
#>>>>>>>>>>>>>>>>> to Check whether the num is Palindrome or not ---- without ffunction--------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# num= int(input("enter the number"))
# num_str = str(num)

# if num_str==num_str[::-1]:
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")
    
    
#>>>>>>>>>>>>>>>>> to Check whether the num is Palindrome or not ---- without ffunction--------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def is_palindrome(num):
#     num_str = str(num)
    
#     return num_str==num_str[::-1]

# num = (input("enter the number or string: "))
# if is_palindrome(num):
#     print(f"'{num}' is Palindrome")
    
# else:
#     print(f"'{num}' is not Palindrome")


###### I.Q....................Program to find factorial of a number.....................................


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# number = int(input("Enter a number: "))

# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"The factorial of {number} is {factorial(number)}.")



### 1.Program to create a class called "Restaurant"
### with attributes for menu items, prices, and ratings, 
### and methods to add and remove items, and to calculate average rating.

# class Restaurent:
#     def __init__(self):
#         self.menu_items = {}
#         self.ratings = []
        
        
#     def add_items(self,items,price):
#         self.menu_items[items] = price
        
        
#     def remove_item(self,item):
        
#         if item in self.menu_items:
#             del self.menu_items[item]
            
            
#     def add_rating(self,rating):
#         self.ratings.append(rating)
        
        
#     def average_rating(self):
#         if sum(self.ratings) / len(self.ratings):
#             return 0
        
        
        
# restaurent = Restaurent()
# restaurent.add_items("Juice",100)
# restaurent.add_items("Shake",50)
# restaurent.add_items("Mojito",35)
# restaurent.add_rating(10)
# restaurent.add_rating(15)


# print("Menu :",restaurent.menu_items)
# print("Average Rating : " ,restaurent.average_rating())



        
        
        
        