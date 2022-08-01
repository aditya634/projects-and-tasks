# Importing mysql 
# Command to install the mysql connector : pip install mysql-connector
import mysql.connector as mysql

# Creating the Connection object with database "demo_data"
con = mysql.connect(host="localhost",user="root",password="",database="demo_data")

# Making cursor object :
curObj = con.cursor()

# Selecting all the details of the table doctor_details :
curObj.execute("SELECT Hospital_Id,Bed_Count from hospital_data ")
# You can change the query according to your need

# fetchall() : It will fetch all the Records from your current record according to the query executed 
#              It will be stored in form of list having tuple of all the records 
records = curObj.fetchall()
print(records)

# Displaying the records fetched !
for i in records:
    for j in i:
        print(j)
    print("---------------")

# for i in records:
#     print("Hospital Id :",i[0])
#     print("Hospital Name :",i[1])
#     print("Bed Count :",i[2])
#     print("-----------------------------")

# Saving all things
con.commit()

# Closing the Database Connection
con.close()