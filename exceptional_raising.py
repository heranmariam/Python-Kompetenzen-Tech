#******************************** Exceptional Raise ***************************************


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> WAPP that takes a user input for age it the age is less than Zero Raise a value error with the msg "age cannot be Negative " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def exceptional_raising():
    age = int (input("enter the age:"))
    if age < 0:
        raise ValueError("age cannot be negative")
    else:
        print ("your age is ", + age)
        
exceptional_raising()