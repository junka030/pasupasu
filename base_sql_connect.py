import mysql.connector as SQLC
from mysql.connector import Error
from mysql.connector import errorcode

"""
Initialising Database Connection
"""
mypw = "";
# connection to database object
mydb = SQLC.connector.connect(
    host = "localhost",
    user = "root",
    password = mypw,
    database = "pasuwarudo"
)
# print(mydb)

# cursor class to execute SQL commands
cursor = mydb.cursor()

# initial create database
# cursor.execute("CREATE DATABASE pasuwarudo")
# cursor.execute("SHOW DATABASES;")
# for x in cursor:
#     print(x)

"""
Run SQL commands
"""
try:
    # SQL statement
    statement ="";

    # run command
    cursor.execute(statement) 

    # commit changes to the database
    mydb.commit() 

    print("Database updated!")

except SQLC.Error as error:

    print("Database update failed! : {}",format(error))

    # revert changes
    mydb.rollback()


"""
Disconnection
"""
# disconnecting from the database 
mydb.close() 