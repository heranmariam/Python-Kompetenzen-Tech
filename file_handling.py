############################ Read Operation ################################

# file = open ("python\sample.txt","r")
# content = file.read()
# print (content)
# file.close()


# >>>>>>>>>>>>>>>>>>>>>>>> -------- file with "with Operation " does not need to close --------


# with open("python\sample.txt","r") as file:
#     content = file.read()
#     print (content)



########################### write Operation ########################### 

# with open ("python\sample.txt","w") as file:
#     file.write("This is a sample text.\n")
#     file.write("This is next sample")


############################## Append Operation #############################

# with open ("python\sample.txt","a") as file:
#     file.write("This is Append Operation.\n")
    


# I.Q)   ---------------------Write a program that reads the contents of a file, replaces all spaces with hyphens (-), 
# and writes the modified content back to the file. --------------------------

#### read cheyth replace all spaces with hyphens cheyan egane yezhuthiya mathi bt write cheyanel vere oru variable create cheyam ---- ath thaaaze soln cheyth vechekunath ##########################
# with open("python\sample.txt","r") as file:
#     content = file.read()
#     print(content.replace(" " , " -"))

####### soln ###########
# with open("python/sample.txt", "r") as file:
#     content = file.read()
# modified_content = content.replace(" ", "-")

# with open("python/sample.txt", "w") as file:
#     file.write(modified_content)
# print("File updated successfully with spaces replaced by hyphens.")



### I.Q) ---------------------- Write a program that replaces a specific word in the file with another word. 
# For example, it replaces "Python" with "JavaScript". ------------------------


