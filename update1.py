import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)

mycursor = mydb.cursor()

name=input("Enter Name: ")
address=input("Enter Address: ")

sql="Update customers set address = %s where name = %s"
val=(address,name)
mycursor.execute(sql,val)
mydb.commit()
print("Record Updated")
