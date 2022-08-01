# Importing mysql module
# Command to install the mysql connector : pip install mysql-connector
import mysql.connector as mysql

# Creating the Connection object with database "demo_data"
con = mysql.connect(host="localhost",user="root",password="",database="demo_data")

# Making cursor object :
curObj = con.cursor()

# ----->> Updating the Records Code <<------

# Executing the "Update query"
curObj.execute("UPDATE hospital_data set Bed_Count=300")

# Display number of records affected 
print(curObj.rowcount,'Rows Updated !')

# ----->> Deleting the Records Code <<------

# Executing the "delete query"
curObj.execute("DELETE from hospital_data where Hospital_Id=1")

# Display number of records deleted 
print(curObj.rowcount,'Row Deleted !')

# ----->> Dropping the Table Code <<------

# Executing the "delete query"
# curObj.execute("DROP table hospital_data")

# Display number of records deleted 
# print(curObj.rowcount,'Row Deleted !')

# Saving Things in the Database
con.commit()

# Closing the Database Connection
con.close()