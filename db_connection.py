import mysql.connector
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#ER@N@1999",
        database = "school"
    )
    
    if conn.is_connected():
        print("Connected")
except mysql.connector.Error as e:
    print ("error",e)


    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        position VARCHAR(255),
        salary DECIMAL(10,2)
    )"""
        
    cursor .execute(create_table_query)
    print("Table,'Employees' has been created Successfully")
except mysql.connector.Error as err:
    print("Error: {err}")
    
finally:
        cursor.close()
        conn.close()
        
      ############# insert ################  
        
# try:
    
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="#ER@N@1999",
#         database = "school"
#     )
    
    
#     cursor= conn.cursor()
#     insert_query = """
#     INSERT INTO Employee (name, position, salary) VALUES (%s, %s, %s)
#     """
#     employee_data = [
#         ("John Doe", "Software Engineer", 70000),
#         ("Jane Smith", "Product Manager", 80000),
#         ("Mike Johnson", "Data Scientist", 90000)
#     ]
    
#     cursor.executemany(insert_query, employee_data)
#     conn.commit()
#     print(cursor.rowcount, "records inserted successfully into the Employee table")
    
 
    ################Fetch DATA #################
# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="#ER@N@1999",
#         database = "school"
#     )
    
#     cursor = conn.cursor()
#     fetch_query = " SELECT * FROM Employee "
#     cursor.execute(fetch_query)
#     result = cursor.fetchall()
    
    
#     print("Employees")
#     for row in result:
#         print(row)

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
    
# finally:
#     cursor.close()
#     conn.close()
    
    
    
    ##################### update database #################
    
    
    
# try:
#     conn =mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="#ER@N@1999",
#         database = "school"
#         )
        
        
#     cursor = conn.cursor()
#     update_query = "UPDATE Employee SET salary = %s WHERE name = %s"
#     cursor.execute(update_query,(65000.00,'john doe'))
#     conn.commit()
#     print(f"{cursor.rowcount} row(s) updated successfully")
    
# except mysql.conn.errors as err:
#         print(f"Error: {err}")
        
# finally:
    
#     cursor.close()
#     conn.close()


  
    


