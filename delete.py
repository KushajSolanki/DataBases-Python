import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)

mycursor = mydb.cursor()

mycursor.execute("Delete from customers where name ='Kushaj'")
mydb.commit()
print("Record Deleted")