from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Length Window")
window.geometry('300x200')

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)

mycursor = mydb.cursor()

lbl1 = Label(window,text="Enter Name: ")
lbl1.grid(column=0,row=0)


txt1 = Entry(window, width=30)
txt1.grid(column=1,row=0)

def register():
    name = txt1.get()
    sql = "Delete from customers where name=%s"
    val = (name,)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Register Window', 'Deleted Successfully')

btn = Button(window,text="Enter",bg="orange",fg="black",command=register);
btn.grid(column=1,row=5)

window.mainloop()