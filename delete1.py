import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)

mycursor = mydb.cursor()

name=input("Enter name: ")

sql="Delete from customers where name=%s"
val=(name,)
mycursor.execute(sql,val)
mydb.commit()
print("Record Deleted")
