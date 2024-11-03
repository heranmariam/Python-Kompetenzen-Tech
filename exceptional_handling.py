#******************************* EXCEPTIONAL HANDLING ***************************************

# def exceptional_Handling():
#     try:
#         num1=int(input("Enter the number1: "))
#         num2=int(input("Enter the number2: "))
#         result = num1/num2
#     except ZeroDivisionError:  ####### 4/0 oke cheyumbha olla error mathrame veru bhaki error kannanel ee zeroDivisonError kodukendaa apo bhaki errorum verum like 4/4.5 cheyumbha olla value errror oke print aavum "ZERODIVIONERROR kodutha aa particular error mathrame print aaku"############
#         print("zero division not implemented")
#     except ValueError:
#         print("value error not implemented")
#     else:
#         print("result:",result)
    
# exceptional_Handling()


#>>>>>>>>>>>>>>>>>>...... write a python program that convert a string input to an integer and divides 100 by that integer , handle both diviosn by zero and invalid input type.......................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def exceptional_Handling():
#     try:
#         num1=int(input("Enter the number1: "))
#         result= 100/num1
#     except ZeroDivisionError:
#         print("zero division error not implemented")
#     except ValueError:
#         print("value error not implemented")
#     else:
#         print ("result:",result)
        
# exceptional_Handling()


#...............>>>>>>>> OR >>>>>>>>>>>>>>>>>..................

# def exceptional_Handling():
#     try:
#         num1=int(input("Enter the number1: "))
#         result= 100/num1
#     except (ZeroDivisionError,ValueError):
#         print("zero division error and value error not implemented")

#         print ("result:",result)
        
# exceptional_Handling()




#.....................>>>>>>>>>>>>>>>>>>> write a python program  that attempts to open a file that doesnt exist user generic Except block to handle any error that occur and display a message ....................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def exceptional_file_handling():
    try:
        file = open('non_existent_file.txt', 'r')
        content = file.read()
    # except FileNotFoundError:
    #     print("The file does not exist.")
    
    except :
        print("An error occurred.")
        
    finally:
        if "file" in locals():
            file.close()

exceptional_file_handling()



        
    