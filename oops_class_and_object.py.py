# ...............simple example with Cars with attribute.............

# class Cars:
#     def __init__(self,m,p):
#         self.model = m
#         self.price = p
        
# audi = Cars("R",9)
# bmw = Cars ("U",10)
# print(audi.model,audi.price)
# print(bmw.model)


# ...............simple example with person full name with methods which is a behaviour.............


# class Person:
#     def __init__ (self, f_name,l_name):
#         self.first_name = f_name
#         self.last_name = l_name
#     def get_full_name (self):
#         print("full name: ", self.first_name+self.last_name)
# person1 = Person("alice"," johnson")
# person1 = person1.get_full_name()

#  ............... WAPP to define  a class student which has name and age attributes also write a method to add courses and dispaly student detail?

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.courses = []
        
#     def add_course(self, course):
#         self.courses.append(course)
#         # print(f"{course} has been added to {self.name}'s course.")
        
#     def display_info(self):
#         print(f"students: {self.name}")
#         print(f"age: {self.age}")
#         print("course Enrolled: ")
        
        
#         for course in self.courses:
#             print(f"-{course}")
            
#     def remove_course_info(self,course):
#         if (course in self.courses):
        
#             (self.courses.remove(course))
#         else:
#             print("Can't remove course because this course is not Available")       
            
# student1 = Student("Alice", 20)
# student1.add_course("Mathematics")
# student1.add_course("Physics")
# student1.remove_course_info("php")
# student1.display_info()



# WAPP of a library class to add book and dispaly book?


# class Library:
#     def __init__(self):
#         self.books = []
    
#     def add_book(self, title,author):
#         books = {
#             "title": title,
#             "author": author
#         }
#         self.books.append(books)
#         print(f"{title} by {author} has been added to the library.")
        
        
#     def display_book_info(self):
#         print ("books in the library:")
#         for book in self.books:
#             print("- title:" + book["title"] +" Author:"+ book["author"])
            
# library = Library()
# library.add_book("chetan Bhagath", "2 States")
# library.add_book("aroo", "Harry Potter")
# library.display_book_info()
        