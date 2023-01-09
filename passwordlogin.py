from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.title("Length Window")
window.geometry('300x200')

lbl1 = Label(window, text="Enter Name: ")
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Enter password: ")
lbl2.grid(column=0, row=1)

txt1 = Entry(window, width=30)
txt1.grid(column=1, row=0)
txt2 = Entry(window, width=30)
txt2.grid(column=1, row=1)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python2"
)
mycursor = mydb.cursor()
def login():
    user=txt1.get()
    pass1=txt2.get()
    sql="SELECT * FROM passwords where user =%s and pass1=%s"
    val=(user,pass1)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchall()

    print(type(myresult))
    print(len(myresult))

    if(len(myresult)==1):
        messagebox.showinfo('Message title', 'Login Successfully')
        import guidatabase
        window.detroy()
    else:
        messagebox.showinfo('Message title', 'Login failed')

btn = Button(window,text="Enter",bg="orange",fg="black",command=login);
btn.grid(column=1,row=5)
window.mainloop()
