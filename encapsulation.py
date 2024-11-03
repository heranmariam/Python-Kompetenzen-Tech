class Student:
    def __init__ (self,fn,ln,a):
        self.first_name = fn
        self._last_name = ln
        self.__age = a
        
    def get_age(self):
        print(self.__age)

b= Student("alice", "John",40)
print(b.first_name,b._last_name)
b.get_age()