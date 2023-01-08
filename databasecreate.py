import mysql.connector
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("Create Database python2")
print("database created")