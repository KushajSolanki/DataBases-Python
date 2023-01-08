import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)

mycursor = mydb.cursor()

name=input("Enter Name: ")
address=input("Enter Address: ")
sql="Insert into customers values(%s,%s)"
val=(name,address)

mycursor.execute(sql, val)
mydb.commit()
print("record inserted");
