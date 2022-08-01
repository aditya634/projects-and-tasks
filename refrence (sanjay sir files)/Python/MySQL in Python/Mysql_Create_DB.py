# Importing mysql
import mysql.connector

try:
    # Connecting mysql with python
    mycon=mysql.connector.connect(host='localhost',user='root',password="")

    # Creating cursor object for executing commands
    cur=mycon.cursor()

    try:
        # Creating a Database :
        cur.execute('create database data')
        print("Database Created !!")
        
        # Dropping(Deleting) the Database
        # cur.execute('drop database data')
        # print("Database Dropped !!")
    except Exception as e:
        print("Database Not Created !!")
        print(e)

    # Saving all the things
    mycon.commit()

    # Closing the Connection
    mycon.close()

except Exception as e:
    print("Connection Failed !!")
    print(e)