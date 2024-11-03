# def function_name():
#     print("hello")
# function_name()



# def greet(name):
#     print ("greetings, " + name,)
# greet ("john")


################################################################  default aait function call cheyan #################################################################


# def greet(name="john"):
#     print ("hello, " + name)
# greet()


################################  return function #################################################################

# def greet(a,b):
#     c=a+b
#     return c
# a= greet (2,4)
# print (a)


# =======>>>>>>>>>>>>>>>>>>>>>> write a python program to find sum of given numbers is in the list or not================>>>>>>>>>>>>>>


def sum_in_list (a,b,c):
    sum=a+b
    if sum in c:
        print (f"the sum of {a}and {b}in {c} and it is in the list")
    else:
        print (f"the sum of {a} and {b}in {c} and it is not in the list")
        
sum_in_list(2,3,[1,2,3,4,6])
   







