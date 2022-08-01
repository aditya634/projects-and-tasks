# Importing mysql 
# Command to install the mysql connector : pip install mysql-connector-python
import mysql.connector as mysql

# Creating the Connection object with database "demo_data"
con = mysql.connect(host="localhost",user="root",password="",database="demo_data")

# Making cursor object :
curObj = con.cursor()

# Creating hospital_data table :
# we use execute() to execute/implement one query

# If we want to change database here :
# curObj.execute("use demo_data")

curObj.execute("CREATE TABLE IF NOT EXISTS hospital_data(Hospital_Id INT, Hospital_Name Varchar(30), Bed_Count INT)")

# Records that we have to add in the table
hospital_records=[(1,'Janta',200),
                  (2,'Zydus',500),
                  (3,'Sal',1000),
                  (4,'Stirling',1500)]

curObj.execute("insert into hospital_data values(0,\"Civil\",900)");

# Inserting the records in table "hospital_data"
# executemany() : Used to execute the query many times according to the list
#                 Used to insert many records in the table 
# curObj.executemany('<command>',<list-of-records>)

# Displaying number of row added in Table
# rowcount : Used to display how many rows are affected/created
print(curObj.rowcount,'records Inserted in hospital_data !')

# Saving Things in the Database
con.commit()

# Closing the Database Connection
con.close()
