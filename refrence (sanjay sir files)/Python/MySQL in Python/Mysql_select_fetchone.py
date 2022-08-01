# Importing mysql 
# Command to install the mysql connector : pip install mysql-connector
import mysql.connector as mysql

# Creating the Connection object with database "demo_data"
con = mysql.connect(host="localhost",user="root",password="",database="demo_data")

# Making cursor object :
curObj = con.cursor()

# Selecting all the details of the table hospital_data :
curObj.execute("SELECT * from hospital_data")
# You can change the query according to your need

# fetchone() : It will fetch only one Records according to the query executed at a time
#              It will be stored in form of tuple
record1 = curObj.fetchone()

# Displaying the first record : !
print("1st Record : ",record1)

record2 = curObj.fetchone()

# Displaying the second record !
print("2nd Record : ",record2)

remRecords = curObj.fetchall()

for i in remRecords:
    print(i)
# Closing the Database Connection
con.close()