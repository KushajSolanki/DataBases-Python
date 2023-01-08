import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)
mycursor = mydb.cursor()
mycursor.execute("Insert into customers values('admin','Nashik')")
mydb.commit()
print("Record inserted")
