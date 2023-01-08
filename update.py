import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)

mycursor = mydb.cursor()

mycursor.execute("Update customers set address='Pune' where name='admin'")
mydb.commit()
print("Record Updated")