class Student:
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